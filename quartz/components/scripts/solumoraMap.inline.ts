import { ContentDetails } from "../../plugins/emitters/contentIndex"
import { FullSlug, resolveRelative } from "../../util/path"

type ContentIndex = Record<string, ContentDetails>
type MarkerElement = SVGAElement & {
  dataset: {
    mapKeys?: string
    mapTitles?: string
    mapLabel?: string
  }
}

const REFRESH_INTERVAL_MS = 45000

function splitList(raw: string | undefined): string[] {
  if (!raw) {
    return []
  }

  return raw
    .split("|")
    .map((entry) => entry.trim())
    .filter((entry) => entry.length > 0)
}

function normalize(input: string): string {
  return input.toLowerCase().replace(/[^a-z0-9]/g, "")
}

async function fetchLatestIndex(currentSlug: FullSlug): Promise<ContentIndex> {
  const fallback = await fetchData
  const indexPath = `${resolveRelative(currentSlug, "static/contentIndex" as FullSlug)}.json`

  try {
    const response = await fetch(`${indexPath}?ts=${Date.now()}`, { cache: "no-store" })
    if (!response.ok) {
      return fallback
    }

    return (await response.json()) as ContentIndex
  } catch {
    return fallback
  }
}

function findEntry(
  index: ContentIndex,
  keyCandidates: string[],
  titleCandidates: string[],
): [string, ContentDetails] | undefined {
  for (const key of keyCandidates) {
    const entry = index[key]
    if (entry) {
      return [key, entry]
    }
  }

  if (titleCandidates.length === 0) {
    return undefined
  }

  const titleSet = new Set(titleCandidates.map((title) => normalize(title)))
  for (const [slug, details] of Object.entries(index)) {
    if (titleSet.has(normalize(details.title))) {
      return [slug, details]
    }
  }

  return undefined
}

function stampNow(): string {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  })
}

async function refreshMap(mapRoot: HTMLElement, currentSlug: FullSlug) {
  const status = mapRoot.querySelector(".solumora-map-status") as HTMLElement | null
  if (status) {
    status.textContent = "Syncing map links..."
  }

  const index = await fetchLatestIndex(currentSlug)
  const markers = Array.from(
    mapRoot.querySelectorAll(".solumora-map-marker"),
  ) as unknown as MarkerElement[]
  let linkedCount = 0

  for (const marker of markers) {
    const keys = splitList(marker.dataset.mapKeys)
    const titles = splitList(marker.dataset.mapTitles)
    const match = findEntry(index, keys, titles)
    const defaultLabel = marker.dataset.mapLabel ?? "Mapped location"

    if (!match) {
      marker.classList.add("is-missing")
      marker.classList.remove("is-active")
      marker.setAttribute("aria-label", `${defaultLabel} (unresolved link target)`)
      marker.removeAttribute("href")
      continue
    }

    const [targetSlug, details] = match
    marker.classList.add("is-active")
    marker.classList.remove("is-missing")
    marker.setAttribute("href", resolveRelative(currentSlug, targetSlug as FullSlug))
    marker.setAttribute("aria-label", `Open ${details.title}`)
    linkedCount += 1
  }

  if (status) {
    status.textContent = `Synced ${stampNow()} - ${linkedCount}/${markers.length} map points resolved`
  }
}

function setupMaps(currentSlug: FullSlug) {
  const mapRoots = document.querySelectorAll(
    "[data-solumora-map='true']",
  ) as NodeListOf<HTMLElement>
  for (const mapRoot of mapRoots) {
    const refreshButton = mapRoot.querySelector(".solumora-map-refresh") as HTMLButtonElement | null
    const refreshFn = () => {
      refreshMap(mapRoot, currentSlug)
    }

    refreshFn()

    if (refreshButton) {
      refreshButton.addEventListener("click", refreshFn)
      window.addCleanup(() => refreshButton.removeEventListener("click", refreshFn))
    }

    const intervalId = window.setInterval(refreshFn, REFRESH_INTERVAL_MS)
    window.addCleanup(() => window.clearInterval(intervalId))
  }
}

document.addEventListener("nav", (e: CustomEventMap["nav"]) => {
  setupMaps(e.detail.url)
})

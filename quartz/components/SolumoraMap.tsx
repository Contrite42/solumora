import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
// @ts-ignore
import script from "./scripts/solumoraMap.inline"
import style from "./styles/solumoraMap.scss"

type MarkerAlignment = "left" | "right"

interface MapMarker {
  id: string
  label: string
  x: number
  y: number
  keys: string[]
  titles: string[]
  align?: MarkerAlignment
}

const MAP_MARKERS: MapMarker[] = [
  {
    id: "wolfpoint",
    label: "Wolfpoint",
    x: 490,
    y: 102,
    keys: ["Wolfpoint"],
    titles: ["Wolfpoint"],
    align: "right",
  },
  {
    id: "greyveil",
    label: "Greyveil",
    x: 462,
    y: 220,
    keys: ["Greyveil"],
    titles: ["Greyveil"],
    align: "right",
  },
  {
    id: "valdenmoor",
    label: "Valdenmoor",
    x: 500,
    y: 382,
    keys: ["Valdenmoor"],
    titles: ["Valdenmoor"],
    align: "right",
  },
  {
    id: "ashford",
    label: "Ashford",
    x: 756,
    y: 468,
    keys: ["Ashford"],
    titles: ["Ashford"],
    align: "left",
  },
  {
    id: "northern-narrows",
    label: "Northern Narrows",
    x: 676,
    y: 620,
    keys: ["The-Northern-Narrows", "Northern-Narrows"],
    titles: ["The Northern Narrows", "Northern Narrows"],
    align: "left",
  },
  {
    id: "equatorial-desert",
    label: "Desert Zakros",
    x: 500,
    y: 770,
    keys: ["Equatorial-Desert"],
    titles: ["Equatorial Desert", "Desert Zakros"],
    align: "right",
  },
  {
    id: "southern-approaches",
    label: "Southern Approaches",
    x: 660,
    y: 902,
    keys: ["The-Southern-Approaches", "Southern-Approaches"],
    titles: ["The Southern Approaches", "Southern Approaches"],
    align: "left",
  },
  {
    id: "halveth",
    label: "Halveth",
    x: 648,
    y: 958,
    keys: ["Halveth"],
    titles: ["Halveth"],
    align: "left",
  },
  {
    id: "solhaven",
    label: "Solhaven",
    x: 244,
    y: 1164,
    keys: ["Solhaven"],
    titles: ["Solhaven"],
    align: "right",
  },
  {
    id: "hedun",
    label: "Hedun",
    x: 192,
    y: 1280,
    keys: ["Hedun"],
    titles: ["Hedun"],
    align: "right",
  },
]

export default (() => {
  const SolumoraMap: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
    return (
      <section class={classNames(displayClass, "solumora-map")} data-solumora-map="true">
        <div class="solumora-map-header">
          <h2>Live Continental Map</h2>
          <button type="button" class="solumora-map-refresh">
            Refresh
          </button>
        </div>
        <p class="solumora-map-status" aria-live="polite">
          Syncing map links...
        </p>
        <svg
          class="solumora-map-svg"
          viewBox="0 0 1000 1500"
          role="img"
          aria-label="Solumora continental map with canonical positions of key regions and settlements."
        >
          <defs>
            <filter id="solumora-map-shadow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="6" stdDeviation="8" flood-opacity="0.2" />
            </filter>
          </defs>

          <path
            class="solumora-map-continent"
            d="M420 40 L575 40 L675 115 L760 250 L826 430 L853 630 L841 856 L804 1044 L756 1220 L672 1368 L572 1458 L432 1458 L322 1365 L250 1216 L196 1024 L157 854 L147 640 L174 444 L250 260 L335 120 Z"
            filter="url(#solumora-map-shadow)"
          />

          <rect class="solumora-zone solumora-zone--north" x="220" y="154" width="560" height="452" rx="26" />
          <rect class="solumora-zone solumora-zone--desert" x="194" y="618" width="610" height="304" rx="26" />
          <rect class="solumora-zone solumora-zone--south" x="196" y="936" width="590" height="452" rx="26" />

          <text class="solumora-zone-label" x="500" y="222">
            Terravelle Uplands
          </text>
          <text class="solumora-zone-label" x="500" y="776">
            Equatorial Desert Zakros
          </text>
          <text class="solumora-zone-label" x="500" y="1024">
            Auralis Basin
          </text>

          {MAP_MARKERS.map((marker) => {
            const alignment = marker.align ?? "right"
            const textAnchor = alignment === "left" ? "end" : "start"
            const textX = alignment === "left" ? -14 : 14
            return (
              <a
                class={`solumora-map-marker solumora-map-marker--${alignment}`}
                data-map-marker={marker.id}
                data-map-keys={marker.keys.join("|")}
                data-map-titles={marker.titles.join("|")}
                data-map-label={marker.label}
                transform={`translate(${marker.x} ${marker.y})`}
                href="#"
              >
                <circle r="8" />
                <text x={textX} y="4" text-anchor={textAnchor}>
                  {marker.label}
                </text>
              </a>
            )
          })}
        </svg>
        <p class="solumora-map-note">
          Positions follow current canon: north-south elevation, the full-width Zakros barrier, and
          coast-facing route hubs.
        </p>
      </section>
    )
  }

  SolumoraMap.css = style
  SolumoraMap.afterDOMLoaded = script

  return SolumoraMap
}) satisfies QuartzComponentConstructor

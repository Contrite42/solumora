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
  labelDx?: number
  labelDy?: number
}

interface ZoneBand {
  id: string
  label: string
  y: number
  height: number
  labelX: number
  labelY: number
}

const CONTINENT_PATH =
  "M420 40 L575 40 L675 115 L760 250 L826 430 L853 630 L841 856 L804 1044 L756 1220 L672 1368 L572 1458 L432 1458 L322 1365 L250 1216 L196 1024 L157 854 L147 640 L174 444 L250 260 L335 120 Z"

const ZONE_BANDS: ZoneBand[] = [
  {
    id: "north",
    label: "Terravelle Uplands",
    y: 150,
    height: 470,
    labelX: 250,
    labelY: 290,
  },
  {
    id: "desert",
    label: "Equatorial Desert Zakros",
    y: 620,
    height: 300,
    labelX: 228,
    labelY: 790,
  },
  {
    id: "south",
    label: "Auralis Basin",
    y: 920,
    height: 500,
    labelX: 250,
    labelY: 1080,
  },
]

const MAP_MARKERS: MapMarker[] = [
  {
    id: "wolfpoint",
    label: "Wolfpoint",
    x: 500,
    y: 108,
    keys: ["Wolfpoint"],
    titles: ["Wolfpoint"],
    align: "right",
  },
  {
    id: "greyveil",
    label: "Greyveil",
    x: 390,
    y: 268,
    keys: ["Greyveil"],
    titles: ["Greyveil"],
    align: "right",
  },
  {
    id: "valdenmoor",
    label: "Valdenmoor",
    x: 480,
    y: 412,
    keys: ["Valdenmoor"],
    titles: ["Valdenmoor"],
    align: "right",
  },
  {
    id: "ashford",
    label: "Ashford",
    x: 748,
    y: 498,
    keys: ["Ashford"],
    titles: ["Ashford"],
    align: "left",
  },
  {
    id: "northern-narrows",
    label: "Northern Narrows",
    x: 688,
    y: 666,
    keys: ["The-Northern-Narrows", "Northern-Narrows"],
    titles: ["The Northern Narrows", "Northern Narrows"],
    align: "left",
  },
  {
    id: "equatorial-desert",
    label: "Desert Zakros",
    x: 628,
    y: 790,
    keys: ["Equatorial-Desert"],
    titles: ["Equatorial Desert", "Desert Zakros"],
    align: "left",
    labelDy: -10,
  },
  {
    id: "southern-approaches",
    label: "Southern Approaches",
    x: 684,
    y: 906,
    keys: ["The-Southern-Approaches", "Southern-Approaches"],
    titles: ["The Southern Approaches", "Southern Approaches"],
    align: "left",
  },
  {
    id: "halveth",
    label: "Halveth",
    x: 690,
    y: 980,
    keys: ["Halveth"],
    titles: ["Halveth"],
    align: "left",
  },
  {
    id: "solhaven",
    label: "Solhaven",
    x: 232,
    y: 1166,
    keys: ["Solhaven"],
    titles: ["Solhaven"],
    align: "right",
  },
  {
    id: "hedun",
    label: "Hedun",
    x: 188,
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
            <clipPath id="solumora-continent-clip">
              <path d={CONTINENT_PATH} />
            </clipPath>
          </defs>

          <path class="solumora-map-continent" d={CONTINENT_PATH} filter="url(#solumora-map-shadow)" />

          <g class="solumora-zone-bands" clip-path="url(#solumora-continent-clip)">
            {ZONE_BANDS.map((zone) => (
              <rect
                class={`solumora-zone solumora-zone--${zone.id}`}
                x="140"
                y={zone.y}
                width="740"
                height={zone.height}
                rx="0"
              />
            ))}

            <line class="solumora-lat-line" x1="150" x2="850" y1="620" y2="620" />
            <line class="solumora-lat-line" x1="150" x2="850" y1="920" y2="920" />
          </g>

          <path class="solumora-route solumora-route--zakros" d="M688 666 C668 744 670 840 684 906" />

          <g class="solumora-zone-labels">
            {ZONE_BANDS.map((zone) => (
              <g class={`solumora-zone-tag solumora-zone-tag--${zone.id}`} transform={`translate(${zone.labelX} ${zone.labelY})`}>
                <rect x="-8" y="-23" width="274" height="36" rx="10" />
                <text class="solumora-zone-label" x="129" y="1">
                  {zone.label}
                </text>
              </g>
            ))}
          </g>

          {MAP_MARKERS.map((marker) => {
            const alignment = marker.align ?? "right"
            const textAnchor = alignment === "left" ? "end" : "start"
            const textX = marker.labelDx ?? (alignment === "left" ? -14 : 14)
            const textY = marker.labelDy ?? 4
            const lineX1 = alignment === "left" ? -5 : 5
            const lineX2 = alignment === "left" ? -11 : 11
            return (
              <g transform={`translate(${marker.x} ${marker.y})`}>
                <a
                  class={`solumora-map-marker solumora-map-marker--${alignment}`}
                  data-map-marker={marker.id}
                  data-map-keys={marker.keys.join("|")}
                  data-map-titles={marker.titles.join("|")}
                  data-map-label={marker.label}
                  href="#"
                >
                  <line x1={lineX1} y1="0" x2={lineX2} y2="0" />
                  <circle r="8" />
                  <text x={textX} y={textY} text-anchor={textAnchor}>
                    {marker.label}
                  </text>
                </a>
              </g>
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

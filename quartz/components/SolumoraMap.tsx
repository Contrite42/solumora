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
  labelWidth: number
}

interface RegionLink {
  id: string
  label: string
  path: string
  keys: string[]
  titles: string[]
  labelX: number
  labelY: number
  labelAnchor?: "start" | "middle" | "end"
  showLabel?: boolean
}

const CONTINENT_PATH =
  "M420 40 L575 40 L675 115 L760 250 L826 430 L853 630 L841 856 L804 1044 L756 1220 L672 1368 L572 1458 L432 1458 L322 1365 L250 1216 L196 1024 L157 854 L147 640 L174 444 L250 260 L335 120 Z"

const ZONE_BANDS: ZoneBand[] = [
  {
    id: "north",
    label: "Terravelle Uplands",
    y: 150,
    height: 430,
    labelX: 218,
    labelY: 292,
    labelWidth: 258,
  },
  {
    id: "frontier",
    label: "Disputed Desert Edge",
    y: 580,
    height: 66,
    labelX: 220,
    labelY: 616,
    labelWidth: 250,
  },
  {
    id: "desert",
    label: "Desert Zakros (Equatorial Belt)",
    y: 646,
    height: 286,
    labelX: 194,
    labelY: 790,
    labelWidth: 336,
  },
  {
    id: "south",
    label: "Auralis Basin",
    y: 932,
    height: 488,
    labelX: 232,
    labelY: 1086,
    labelWidth: 226,
  },
]

const REGION_LINKS: RegionLink[] = [
  {
    id: "zakros-region",
    label: "Zakros Crossing Belt",
    path: "M156 648 L846 648 L842 930 L160 930 Z",
    keys: ["Equatorial-Desert"],
    titles: ["Equatorial Desert", "Desert Zakros"],
    labelX: 500,
    labelY: 782,
    labelAnchor: "middle",
    showLabel: false,
  },
  {
    id: "northern-narrows-region",
    label: "Northern Narrows Corridors",
    path: "M648 588 L770 588 L752 748 L636 748 Z",
    keys: ["The-Northern-Narrows", "Northern-Narrows"],
    titles: ["The Northern Narrows", "Northern Narrows"],
    labelX: 746,
    labelY: 676,
    labelAnchor: "end",
    showLabel: true,
  },
]

const MOUNTAIN_RIDGES = [
  "M404 112 L448 82 L494 112 L538 76 L584 112",
  "M430 148 L474 122 L518 148 L564 116 L610 148",
]

const MAREN_RIVER_PATH = "M404 250 C430 356 452 438 486 504 C554 566 642 588 740 588"

const EAST_ESTUARY_PATH = "M740 588 C780 600 814 618 844 646"
const WEST_COAST_ROUTE_PATH = "M272 1166 C286 1224 298 1268 308 1310"

const WEST_TERRACE_PATHS = [
  "M204 1090 C286 1060 346 1080 402 1128",
  "M194 1136 C278 1110 344 1128 414 1172",
  "M184 1182 C274 1158 344 1174 426 1212",
]

const MAP_MARKERS: MapMarker[] = [
  {
    id: "wolfpoint",
    label: "Wolfpoint",
    x: 498,
    y: 108,
    keys: ["Wolfpoint"],
    titles: ["Wolfpoint"],
    align: "right",
  },
  {
    id: "greyveil",
    label: "Greyveil",
    x: 392,
    y: 318,
    keys: ["Greyveil"],
    titles: ["Greyveil"],
    align: "right",
  },
  {
    id: "valdenmoor",
    label: "Valdenmoor",
    x: 484,
    y: 504,
    keys: ["Valdenmoor"],
    titles: ["Valdenmoor"],
    align: "right",
  },
  {
    id: "ashford",
    label: "Ashford",
    x: 752,
    y: 588,
    keys: ["Ashford"],
    titles: ["Ashford"],
    align: "left",
  },
  {
    id: "halveth",
    label: "Halveth",
    x: 618,
    y: 612,
    keys: ["Halveth"],
    titles: ["Halveth"],
    align: "left",
  },
  {
    id: "solhaven",
    label: "Solhaven",
    x: 274,
    y: 1166,
    keys: ["Solhaven"],
    titles: ["Solhaven"],
    align: "right",
  },
  {
    id: "emberfall",
    label: "Emberfall",
    x: 548,
    y: 1140,
    keys: ["Emberfall"],
    titles: ["Emberfall"],
    align: "right",
  },
  {
    id: "hedun",
    label: "Hedun",
    x: 308,
    y: 1310,
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

          <path
            class="solumora-map-continent"
            d={CONTINENT_PATH}
            filter="url(#solumora-map-shadow)"
          />

          <g class="solumora-zone-bands" clip-path="url(#solumora-continent-clip)">
            {ZONE_BANDS.map((zone) => (
              <rect
                key={zone.id}
                class={`solumora-zone solumora-zone--${zone.id}`}
                x="140"
                y={zone.y}
                width="740"
                height={zone.height}
                rx="0"
              />
            ))}

            <line class="solumora-lat-line" x1="150" x2="850" y1="580" y2="580" />
            <line class="solumora-lat-line" x1="150" x2="850" y1="646" y2="646" />
            <line class="solumora-lat-line" x1="150" x2="850" y1="932" y2="932" />
          </g>

          <g class="solumora-terrain-layer" clip-path="url(#solumora-continent-clip)">
            {MOUNTAIN_RIDGES.map((ridge, idx) => (
              <path
                key={`ridge-${idx}`}
                class="solumora-terrain solumora-terrain--ridge"
                d={ridge}
              />
            ))}
            <path class="solumora-terrain solumora-terrain--river" d={MAREN_RIVER_PATH} />
            <path class="solumora-terrain solumora-terrain--estuary" d={EAST_ESTUARY_PATH} />
            <path
              class="solumora-terrain solumora-terrain--coast-route"
              d={WEST_COAST_ROUTE_PATH}
            />
            {WEST_TERRACE_PATHS.map((terrace, idx) => (
              <path
                key={`terrace-${idx}`}
                class="solumora-terrain solumora-terrain--terrace"
                d={terrace}
              />
            ))}
          </g>

          <g class="solumora-region-links">
            {REGION_LINKS.map((region) => (
              <a
                key={region.id}
                class={`solumora-map-link solumora-map-region-link solumora-map-region-link--${region.id}`}
                data-map-marker={region.id}
                data-map-keys={region.keys.join("|")}
                data-map-titles={region.titles.join("|")}
                data-map-label={region.label}
                href="#"
              >
                <path d={region.path} />
                {region.showLabel ? (
                  <text
                    class="solumora-region-label"
                    x={region.labelX}
                    y={region.labelY}
                    text-anchor={region.labelAnchor ?? "middle"}
                  >
                    {region.label}
                  </text>
                ) : null}
              </a>
            ))}
          </g>

          <g class="solumora-zone-labels">
            {ZONE_BANDS.map((zone) => (
              <g
                key={`${zone.id}-label`}
                class={`solumora-zone-tag solumora-zone-tag--${zone.id}`}
                transform={`translate(${zone.labelX} ${zone.labelY})`}
              >
                <rect x="-8" y="-23" width={zone.labelWidth} height="36" rx="10" />
                <text class="solumora-zone-label" x={Math.round((zone.labelWidth - 16) / 2)} y="1">
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
              <g key={marker.id} transform={`translate(${marker.x} ${marker.y})`}>
                <a
                  class={`solumora-map-link solumora-map-marker solumora-map-marker--${alignment}`}
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
          Positions follow current canon: full-width Zakros barrier, corridor-style approach
          systems, Halveth on the north desert edge, and coast-facing plus valley-linked hubs.
        </p>
      </section>
    )
  }

  SolumoraMap.css = style
  SolumoraMap.afterDOMLoaded = script

  return SolumoraMap
}) satisfies QuartzComponentConstructor

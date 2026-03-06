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
    height: 470,
    labelX: 218,
    labelY: 292,
    labelWidth: 258,
  },
  {
    id: "desert",
    label: "Desert Zakros (Equatorial Belt)",
    y: 620,
    height: 300,
    labelX: 194,
    labelY: 790,
    labelWidth: 336,
  },
  {
    id: "frontier",
    label: "Disputed Desert Edge",
    y: 920,
    height: 72,
    labelX: 220,
    labelY: 954,
    labelWidth: 250,
  },
  {
    id: "south",
    label: "Auralis Basin",
    y: 992,
    height: 428,
    labelX: 232,
    labelY: 1098,
    labelWidth: 226,
  },
]

const REGION_LINKS: RegionLink[] = [
  {
    id: "zakros-region",
    label: "Zakros Crossing Belt",
    path: "M156 622 L846 622 L842 918 L160 918 Z",
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
    path: "M622 622 L758 622 L744 774 L608 774 Z",
    keys: ["The-Northern-Narrows", "Northern-Narrows"],
    titles: ["The Northern Narrows", "Northern Narrows"],
    labelX: 746,
    labelY: 708,
    labelAnchor: "end",
    showLabel: true,
  },
  {
    id: "southern-approaches-region",
    label: "Southern Approaches Network",
    path: "M598 918 L736 918 L702 1038 L572 1038 Z",
    keys: ["The-Southern-Approaches", "Southern-Approaches"],
    titles: ["The Southern Approaches", "Southern Approaches"],
    labelX: 744,
    labelY: 990,
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
    x: 622,
    y: 968,
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
    id: "emberfall",
    label: "Emberfall",
    x: 542,
    y: 1144,
    keys: ["Emberfall"],
    titles: ["Emberfall"],
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

            <line class="solumora-lat-line" x1="150" x2="850" y1="620" y2="620" />
            <line class="solumora-lat-line" x1="150" x2="850" y1="920" y2="920" />
            <line
              class="solumora-lat-line solumora-lat-line--soft"
              x1="150"
              x2="850"
              y1="992"
              y2="992"
            />
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
          systems, disputed Halveth edge, and coast-facing plus valley-linked hubs.
        </p>
      </section>
    )
  }

  SolumoraMap.css = style
  SolumoraMap.afterDOMLoaded = script

  return SolumoraMap
}) satisfies QuartzComponentConstructor

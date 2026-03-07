import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
// @ts-ignore
import script from "./scripts/solumoraMap.inline"
import style from "./styles/solumoraMap.scss"

/**
 * SolumoraMap Component
 *
 * Interactive SVG map rendering the Solumora continental geography.
 * Features canonical city positions, climate zones, terrain features,
 * and clickable region/location links that connect to wiki pages.
 *
 * Coordinate System: 1000x1500px viewport
 * - North: ~y40 (tundra peaks)
 * - South: ~y1450 (southern basin)
 * - West: ~x140 (western coast)
 * - East: ~x860 (eastern plateau)
 */

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

/**
 * CONTINENT_PATH: South America-inspired continental outline
 * - Northernmost point: ~y40 (Wolfpoint peaks)
 * - Southernmost point: ~y1458 (Auralis southern coast)
 * - Widest point: ~x706 (eastern plateau around y700)
 * - Narrowest point: ~x370 (southern tip, Hedun region)
 */
const CONTINENT_PATH =
  "M420 40 L575 40 L675 115 L760 250 L826 430 L853 630 L841 856 L804 1044 L756 1220 L672 1368 L572 1458 L432 1458 L322 1365 L250 1216 L196 1024 L157 854 L147 640 L174 444 L250 260 L335 120 Z"

/**
 * Climate/Political zones displayed as colored bands across the continent
 * Each zone represents distinct ecological and political regions
 */
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

/**
 * Named regions representing trade corridors, strategic areas, and political zones
 * Each region is defined as an interactive SVG polygon path
 */
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
    // Positioned to contain Ashford (798,640) and Halveth (720,680)
    // Right wall at x780, left/bottom corridor-shaped
    path: "M700 600 L780 600 L740 740 L680 740 Z",
    keys: ["The-Northern-Narrows", "Northern-Narrows"],
    titles: ["The Northern Narrows", "Northern Narrows"],
    labelX: 748,
    labelY: 676,
    labelAnchor: "end",
    showLabel: true,
  },
  {
    id: "southern-approaches-region",
    label: "Southern Approaches Network",
    // Positioned to contain Solhaven (460,1000) and Hedun (280,1140)
    // Forms triangular/trapezoidal approach zone in southwest
    path: "M550 850 L720 850 L540 1060 L380 1060 Z",
    keys: ["The-Southern-Approaches", "Southern-Approaches"],
    titles: ["The Southern Approaches", "Southern Approaches"],
    labelX: 630,
    labelY: 950,
    labelAnchor: "end",
    showLabel: true,
  },
]

/**
 * Terrain Features: Mountains, rivers, trade routes, terraces
 */
const MOUNTAIN_RIDGES = [
  "M404 112 L448 82 L494 112 L538 76 L584 112",
  "M430 148 L474 122 L518 148 L564 116 L610 148",
]

const MAREN_RIVER_PATH =
  "M404 250 C430 356 452 438 486 504 C554 566 660 598 744 626 C776 638 800 644 820 646"

const EAST_ESTUARY_PATH = "M820 646 C832 648 842 646 852 642"

// West Coast Route: connects Solhaven (460,1000) to Hedun (280,1140) via coastal valley
const WEST_COAST_ROUTE_PATH = "M460 1000 C406 1050 350 1090 280 1140"

const WEST_TERRACE_PATHS = [
  "M204 1090 C286 1060 346 1080 402 1128",
  "M194 1136 C278 1110 344 1128 414 1172",
  "M184 1182 C274 1158 344 1174 426 1212",
]

/**
 * City Markers: All settlements positioned canonically on the map
 *
 * Key adjustment notes from design iteration:
 * - Ashford & Halveth: Positioned on Northern Narrows right edge (x~700-800)
 *   to reflect their role as border fortifications and trade access points
 * - Solhaven & Hedun: Positioned in southwest approaches zone
 *   Solhaven on central west coast route, Hedun as western valley terminus
 * - Label alignment: right-aligned labels extend from eastern cities,
 *   left-aligned labels extend from western cities
 */
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
    x: 828,
    y: 640,
    keys: ["Ashford"],
    titles: ["Ashford"],
    align: "left",
  },
  {
    id: "halveth",
    label: "Halveth",
    x: 720,
    y: 630,
    keys: ["Halveth"],
    titles: ["Halveth"],
    align: "left",
  },
  {
    id: "solhaven",
    label: "Solhaven",
    x: 460,
    y: 1000,
    keys: ["Solhaven"],
    titles: ["Solhaven"],
    align: "right",
    labelDx: -20,
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
    x: 280,
    y: 1140,
    keys: ["Hedun"],
    titles: ["Hedun"],
    align: "right",
    labelDx: -18,
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

        {/* Main SVG Canvas */}
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

          {/* Continent Outline */}
          <path
            class="solumora-map-continent"
            d={CONTINENT_PATH}
            filter="url(#solumora-map-shadow)"
          />

          {/* Climate/Political Zone Bands */}
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

            {/* Zone Latitude Dividers */}
            <line class="solumora-lat-line" x1="150" x2="850" y1="580" y2="580" />
            <line class="solumora-lat-line" x1="150" x2="850" y1="646" y2="646" />
            <line class="solumora-lat-line" x1="150" x2="850" y1="932" y2="932" />
          </g>

          {/* Terrain Features Layer */}
          <g class="solumora-terrain-layer" clip-path="url(#solumora-continent-clip)">
            {/* Mountain Ridges */}
            {MOUNTAIN_RIDGES.map((ridge, idx) => (
              <path
                key={`ridge-${idx}`}
                class="solumora-terrain solumora-terrain--ridge"
                d={ridge}
              />
            ))}

            {/* River Systems */}
            <path class="solumora-terrain solumora-terrain--river" d={MAREN_RIVER_PATH} />
            <path class="solumora-terrain solumora-terrain--estuary" d={EAST_ESTUARY_PATH} />

            {/* Trade Routes */}
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

          {/* Clickable Region Polygons */}
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

          {/* Zone Band Labels */}
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

          {/* City Markers with Labels */}
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
          Canonical map showing trade networks, climate zones, and major settlements. Click regions
          or cities to explore connected wiki articles.
        </p>
      </section>
    )
  }

  SolumoraMap.css = style
  SolumoraMap.afterDOMLoaded = script

  return SolumoraMap
}) satisfies QuartzComponentConstructor

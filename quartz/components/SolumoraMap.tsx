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
 * Canon description: "runs roughly north to south, wider at its middle than at either end"
 * Shape: narrow at northern extremes (Wolfpoint), widest at equatorial middle (Desert Zakros),
 * narrowing toward southern coast (but not as narrow as north)
 * - Northernmost point: ~y50 (Wolfpoint peaks)
 * - Southernmost point: ~y1450 (Auralis southern coast)
 * - Widest point: ~x750 (equatorial Desert Zakros region, y~650-800)
 * - Northern narrow: width ~200-220
 * - Southern moderate: width ~350-380
 */
const CONTINENT_PATH =
  "M400 50 L600 50 L650 120 L710 220 L780 380 L840 580 L870 750 L860 920 L820 1080 L750 1240 L650 1360 L560 1450 L440 1450 L340 1360 L250 1240 L190 1080 L150 920 L140 750 L160 580 L220 380 L290 220 L350 120 Z"

/**
 * Climate/Political zones displayed as colored bands across the continent
 * Each zone represents distinct ecological and political regions
 * Adjusted for corrected continent shape (wider at middle, narrowing at both ends)
 */
const ZONE_BANDS: ZoneBand[] = [
  {
    id: "north",
    label: "Terravelle Uplands",
    y: 150,
    height: 450,
    labelX: 220,
    labelY: 310,
    labelWidth: 258,
  },
  {
    id: "frontier",
    label: "Border Settlement Network",
    y: 600,
    height: 70,
    labelX: 196,
    labelY: 635,
    labelWidth: 324,
  },
  {
    id: "desert",
    label: "Desert Zakros (Equatorial Belt)",
    y: 670,
    height: 280,
    labelX: 194,
    labelY: 810,
    labelWidth: 336,
  },
  {
    id: "south",
    label: "Auralis Basin",
    y: 950,
    height: 470,
    labelX: 232,
    labelY: 1100,
    labelWidth: 226,
  },
]

/**
 * Named regions representing trade corridors, strategic areas, and political zones
 * Each region is defined as an interactive SVG polygon path
 * Adjusted for corrected continent shape
 */
const REGION_LINKS: RegionLink[] = [
  {
    id: "zakros-region",
    label: "Zakros Crossing Belt",
    path: "M150 670 L870 670 L860 950 L150 950 Z",
    keys: ["Equatorial-Desert"],
    titles: ["Equatorial Desert", "Desert Zakros"],
    labelX: 500,
    labelY: 810,
    labelAnchor: "middle",
    showLabel: false,
  },
  {
    id: "northern-narrows-region",
    label: "The Northern Narrows",
    // Positioned to contain Ashford (780,640) and Halveth (680,640)
    // Eastern corridor region near border
    path: "M650 600 L800 600 L780 700 L660 700 Z",
    keys: ["The-Northern-Narrows", "Northern-Narrows"],
    titles: ["The Northern Narrows", "Northern Narrows"],
    labelX: 740,
    labelY: 662,
    labelAnchor: "end",
    showLabel: true,
  },
  {
    id: "southern-approaches-region",
    label: "The Southern Approaches",
    // Positioned to contain Solhaven (380,1000) and approaches to Hedun
    // Represents interior southbound lanes after Narrows entry
    path: "M550 880 L730 880 L560 1080 L340 1080 Z",
    keys: ["The-Southern-Approaches", "Southern-Approaches"],
    titles: ["The Southern Approaches", "Southern Approaches"],
    labelX: 618,
    labelY: 968,
    labelAnchor: "end",
    showLabel: true,
  },
]

/**
 * Terrain Features: Mountains, rivers, trade routes, terraces
 * Adjusted for corrected continent shape
 */
const MOUNTAIN_RIDGES = [
  "M380 100 L430 70 L480 100 L530 80 L580 100",
  "M400 140 L450 110 L500 140 L550 120 L600 140",
]

const MAREN_RIVER_PATH =
  "M380 240 C420 340 460 440 500 520 C570 590 670 620 760 640"

const EAST_ESTUARY_PATH = "M760 640 C800 645 840 643 870 640"

// West Coast Route: connects Solhaven (380,1000) to Hedun (280,1140) via coastal valley
const WEST_COAST_ROUTE_PATH = "M380 1000 C340 1050 310 1090 280 1140"

const WEST_TERRACE_PATHS = [
  "M200 1100 C280 1070 340 1090 400 1135",
  "M190 1150 C270 1120 330 1140 400 1180",
  "M180 1200 C260 1170 320 1190 390 1230",
]

/**
 * City Markers: All settlements positioned canonically on the map
 *
 * Adjusted for corrected continent shape (wider at equatorial middle, narrowing at both ends):
 * - Wolfpoint: Far northern peak (narrow northern extremes)
 * - Greyveil, Valdenmoor: Terravelle uplands (northern settled belt)
 * - Ashford & Halveth: Northern Narrows border region (eastern edge approaching desert)
 * - Solhaven, Hedun, Emberfall: Auralis basin (southern regions)
 * - Label alignment: right-aligned labels extend from eastern cities,
 *   left-aligned labels extend from western cities
 */
const MAP_MARKERS: MapMarker[] = [
  {
    id: "wolfpoint",
    label: "Wolfpoint",
    x: 500,
    y: 100,
    keys: ["Wolfpoint"],
    titles: ["Wolfpoint"],
    align: "right",
  },
  {
    id: "greyveil",
    label: "Greyveil",
    x: 380,
    y: 300,
    keys: ["Greyveil"],
    titles: ["Greyveil"],
    align: "right",
  },
  {
    id: "valdenmoor",
    label: "Valdenmoor",
    x: 500,
    y: 490,
    keys: ["Valdenmoor"],
    titles: ["Valdenmoor"],
    align: "right",
  },
  {
    id: "ashford",
    label: "Ashford",
    x: 780,
    y: 640,
    keys: ["Ashford"],
    titles: ["Ashford"],
    align: "left",
  },
  {
    id: "halveth",
    label: "Halveth",
    x: 680,
    y: 640,
    keys: ["Halveth"],
    titles: ["Halveth"],
    align: "left",
  },
  {
    id: "solhaven",
    label: "Solhaven",
    x: 380,
    y: 1000,
    keys: ["Solhaven"],
    titles: ["Solhaven"],
    align: "right",
    labelDx: -20,
  },
  {
    id: "emberfall",
    label: "Emberfall",
    x: 520,
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
            <line class="solumora-lat-line" x1="140" x2="870" y1="600" y2="600" />
            <line class="solumora-lat-line" x1="140" x2="870" y1="670" y2="670" />
            <line class="solumora-lat-line" x1="140" x2="870" y1="950" y2="950" />
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

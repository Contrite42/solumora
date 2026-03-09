#!/usr/bin/env node

import chokidar from 'chokidar';
import { exec } from 'child_process';
import { promisify } from 'util';
import path from 'path';
import { fileURLToPath } from 'url';

const execAsync = promisify(exec);
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');

let isBuilding = false;
let pendingRebuild = false;

async function rebuildZip() {
  if (isBuilding) {
    pendingRebuild = true;
    return;
  }

  isBuilding = true;
  pendingRebuild = false;

  try {
    console.log(`[${new Date().toLocaleTimeString()}] Rebuilding solumora-world-content.zip...`);
    
    const command = process.platform === 'win32'
      ? `powershell -Command "Compress-Archive -Path 'content\\*' -DestinationPath 'public\\solumora-world-content.zip' -Force"`
      : `cd "${rootDir}" && zip -r public/solumora-world-content.zip content/`;
    
    await execAsync(command, { cwd: rootDir });
    console.log(`[${new Date().toLocaleTimeString()}] ✓ Zip file rebuilt successfully`);
  } catch (error) {
    console.error(`[${new Date().toLocaleTimeString()}] ✗ Error rebuilding zip:`, error.message);
  } finally {
    isBuilding = false;
    
    // If changes occurred during build, rebuild again
    if (pendingRebuild) {
      setTimeout(rebuildZip, 500);
    }
  }
}

// Watch content directory
const watcher = chokidar.watch('content/**/*', {
  ignored: /(^|[\/\\])\../, // ignore dotfiles
  persistent: true,
  ignoreInitial: true,
  cwd: rootDir
});

watcher
  .on('add', (filePath) => {
    console.log(`[${new Date().toLocaleTimeString()}] File added: ${filePath}`);
    rebuildZip();
  })
  .on('change', (filePath) => {
    console.log(`[${new Date().toLocaleTimeString()}] File changed: ${filePath}`);
    rebuildZip();
  })
  .on('unlink', (filePath) => {
    console.log(`[${new Date().toLocaleTimeString()}] File removed: ${filePath}`);
    rebuildZip();
  })
  .on('ready', () => {
    console.log('👁️  Watching content/ directory for changes...');
    console.log('   Press Ctrl+C to stop');
  })
  .on('error', (error) => {
    console.error(`Watcher error: ${error}`);
  });

// Handle graceful shutdown
process.on('SIGINT', () => {
  console.log('\n\nStopping content watcher...');
  watcher.close();
  process.exit(0);
});

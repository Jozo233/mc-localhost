import { Command } from 'commander';
import { readFile } from 'node:fs/promises';

import setup from './commands/setup';

const mclocalhost = new Command('mclocalhost');

const packajeJson = new URL('../package.json', import.meta.url);
const version = JSON.parse(await readFile(packajeJson, 'utf-8')).version;

mclocalhost.version(version);

mclocalhost
    .command('setup')
    .description('Setup your server')
    .action(setup);

// TODO: RUN

mclocalhost.parse(process.argv);
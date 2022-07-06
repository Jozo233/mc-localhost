import { setupPrompt } from '../prompts/setupPrompt';
import { mkdir, writeFile } from 'node:fs/promises';
import process from 'node:process';
// import { fetch } from 'undici'; // TODO: FINISH
import prompts from 'prompts';
import runJob from '../utils/runJob';

export default async () => {
	const response = await prompts(setupPrompt());

	const jobs: [() => any, string][] = [
		[() => mkdir('server'), 'Creating folder'],
		[() => setupServerProperties(response), 'Setuping server.properties'],
		[() => downloadServerJar(), 'Downloading server jar'],
	];

	for (const [job, message] of jobs) {
		await runJob(job, message).catch(() => process.exit(1));
	}
};

export const setupServerProperties = response => {
	return new Promise(resolve => {
		const data = [
			`server-port=${response['server-port']}`,
			`max-players=${response['max-players']}`,
			`online-mode=${response['online-mode']}`,
		].join('\n');

		writeFile('server/server.properties', data);
		resolve(true);
	});
};

export const getLastSuccessfulBuild = () => {
	return new Promise(resolve => {
		// TODO: FINISH IT

		resolve(true);
	});
};

export const downloadServerJar = () => {
	return new Promise(resolve => {
		// TODO: FINISH IT

		resolve(true);
	});
};

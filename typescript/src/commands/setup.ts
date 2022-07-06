import { setupPrompt } from '../prompts/setupPrompt';
import { mkdir, writeFile } from 'node:fs/promises';
import { fetch } from 'undici'; // TODO: FINISH
import prompts from 'prompts';
import runJob from '../utils/runJob';

export default async() => {
    const response = await prompts(setupPrompt());

	const jobs: [() => any, string][] = [
        [() => mkdir('server'), `Creating folder`],
        [() => setupServerProperties(response), `Setuping server.properties`],
		[() => downloadServerJar(response), `Downloading server jar`]
	];

	for (const [job, message] of jobs) {
		await runJob(job, message).catch(() => process.exit(1));
	}
}

export const setupServerProperties = (response) => {
    return new Promise(async(resolve) => {
        const data = [
            `server-port=${response['server-port']}`,
            `max-players=${response['max-players']}`,
            `online-mode=${response['online-mode']}`
        ].join('\n');

        writeFile(`server/server.properties`, data);
        resolve(true);
    })
}

export const getLastSuccessfulBuild = () => {
	return new Promise(async(resolve) => {
        // TODO: FINISH IT
		
		resolve(true);
	});
}

export const downloadServerJar = (response) => {
	return new Promise(async(resolve) => {
        // TODO: FINISH IT
		
		resolve(true);
	});
};
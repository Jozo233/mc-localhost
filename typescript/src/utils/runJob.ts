// https://github.com/Garlic-Team/gcommands-cli/blob/master/src/utils/runJob.ts
import ora from 'ora';

export default (job: () => Promise<any>, message) => {
	return new Promise((resolve, reject) => {
		const spinner = ora(message).start();

		return job()
			.then((data) => {
				spinner.succeed();

				if (typeof data !== 'boolean') resolve(data);
				else resolve(true);
			})
			.catch((e) => {
				spinner.fail(e);
				reject(e);
			});
	});
};
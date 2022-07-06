import process from 'node:process';

export default (text: string): void => {
	process.stdout.write(text);
};

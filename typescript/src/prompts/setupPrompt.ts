import type { PromptObject } from 'prompts';
import fs from 'fs';

export const setupPrompt = (): Array<PromptObject> => {
	return [
		{
			type: 'text',
			name: 'server-port',
			message: 'Jaký mám používat port?',
            initial: '25565',
			validate: (value) => value.length <= 5
		},
        {
            type: 'number',
            name: 'max-players',
            message: 'Pro kolik hráčů má být server?',
            initial: 100
        },
        {
            type: 'toggle',
            name: 'online-mode',
            message: 'Má být povolen režim online (warez hráči)?',
            initial: 'false'
        }
        // TODO: CUSTOM CONFIG WITH JAVA ARGUMENTS
	];
};
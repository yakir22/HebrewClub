import { getWeek } from 'date-fns';
import fs from 'fs';
export interface ITextEntity {
	type: string;
	text: string;
}


interface ITelegramTextEntry {
	type: string;
	text: string;
	from_id: string;
	from?: string;
	date_unixtime: number;
	date?: string;
	id: number;
	reply_to_message_id?: number;
	text_entities?: ITextEntity[];
	file?: string;
	media_type?: string;
	mime_type?: string;
	duration_seconds?: number,
}

const data = require('../data/result.json');
console.log(data.messages.length);


let messages: ITelegramTextEntry[] = data.messages.filter((message: ITelegramTextEntry) => message.from === 'Ali');

interface IExcersize {
	titleMessage: ITelegramTextEntry;
	questionMessage: ITelegramTextEntry;
	voiceMessage: ITelegramTextEntry;
	videoMessage?: ITelegramTextEntry;
	otherMessages?: ITelegramTextEntry[];
}
// search for a messge that contains a file and extract the message and the previous two messages
const excersizes: IExcersize[] = [];
// messages = messages.filter()
messages.forEach((message, index) => {
	if (message.file && message.media_type?.includes('voice')) {
		const excersize: IExcersize = {
			titleMessage: messages[index - 2],
			questionMessage: messages[index - 1],
			voiceMessage: message,
		};
		excersizes.push(excersize);
	}
});

for (let i = 0; i < excersizes.length - 1; i++) {
	excersizes[i].otherMessages = data.messages.filter((message: ITelegramTextEntry) =>
		message.id > excersizes[i].titleMessage.id &&
		message.id < excersizes[i + 1].titleMessage.id &&
		message.from !== 'Ali' &&
		!message.from?.includes('Hebrew Cookie')
	);
	excersizes[i].otherMessages = JSON.parse(JSON.stringify(excersizes[i].otherMessages));
}
excersizes[excersizes.length - 1].otherMessages = data.messages.filter((message: ITelegramTextEntry) =>
	message.id > excersizes[excersizes.length - 1].titleMessage.id &&
	message.from !== 'Ali' &&
	!message.from?.includes('Hebrew Cookie')
);
excersizes[excersizes.length - 1].otherMessages = JSON.parse(JSON.stringify(excersizes[excersizes.length - 1].otherMessages));

// TODO :: match reply to message id and move message to proper place
excersizes.forEach((excersize) => {
	//console.log({ t0: excersize.titleMessage.text, t1: excersize.questionMessage.text, v0: excersize.voiceMessage.file });
	excersize.otherMessages?.forEach(otherMessage => {
		otherMessage.text = otherMessage.text_entities!.map(ent => ent.text.trim()).join(' ').replaceAll('  ', ' ');
		delete otherMessage.text_entities;
		delete otherMessage.from;
		delete otherMessage.date;
	});
});

// group excersizes that happened in the same calendar week but start on Sundat inseatd of Monday
const groupedExcersizes: { [k: number]: IExcersize[] } = {};
const arrayOfAny: IExcersize[][] = [];
excersizes.forEach((excersize) => {
	const date = new Date(excersize.titleMessage.date_unixtime * 1000);
	const weekNumber = getWeek(date, { weekStartsOn: 0 }); // Week starts on Sunday
	if (!groupedExcersizes[weekNumber]) {
		groupedExcersizes[weekNumber] = [];
		arrayOfAny.push(groupedExcersizes[weekNumber]);
	}
	groupedExcersizes[weekNumber].push(excersize);
});

const finalArray: IOneEntry[][] = [];
arrayOfAny.forEach(week => {
	if (week.length > 1) {
		console.log('-----------------');
		const tempArray: IOneEntry[] = [];
		week.forEach(excersize => {
			if (excersize.questionMessage.id == 626) {
				// debugger
			}
			let qm = excersize.questionMessage.text_entities!.map(ent => ent.text).join(' ');
			if (qm.length == 0) {
				qm = excersize.titleMessage.text_entities!.map(ent => ent.text).join(' ');
			}
			const qma = qm.split('\n\n');
			let t1 = qma[0]?.split('\n');
			let t2 = qma[1]?.split('\n');
			if (qma[0].includes('יום') && qma[0].length < 10) {
				// if (!qma[0].includes('יום'))
				// 	debugger;
				t1 = qma[1]?.split('\n');
				t2 = qma[2]?.split('\n');
			}
			if (t1[0].includes('?') && t2.length > 3) {
				tempArray.push({
					t0id: excersize.titleMessage.id,
					t1id: excersize.questionMessage.id,
					t0: excersize.titleMessage.text_entities!.map(ent => ent.text).join(' ').split('\n\n')[0]?.split('\n'),
					t00: excersize.titleMessage.text_entities!.map(ent => ent.text).join(' ').split('\n\n')[1]?.split('\n') ?? excersize.titleMessage.text,
					t1,
					t2: t2.map(ent => ent.split('-')), /*v0: excersize.voiceMessage.file*/
					otherMessages: excersize.otherMessages?.filter(ent => ent.text.length > 200),
				});
			} else {
				console.log('verify:', excersize);
			}
		})
		finalArray.push(tempArray);
	}
});

interface IOneEntry {
	t1: string[];
	t2: string[][];
	t0id: number;
	t1id: number;
	t0: string[];
	t00: any;
	otherMessages?: ITelegramTextEntry[];
}


fs.writeFileSync('./data/groupedExcersizes.json', JSON.stringify(finalArray, null, 2));

const stringToTss: string[] = [];
finalArray.forEach((week) => {
	week.forEach((excersize) => {
		stringToTss.push(...(excersize.t1));
		stringToTss.push(...(excersize.t2.map(ent => ent[0])));
	});
});


fs.writeFileSync('./data/stringToTss.json', JSON.stringify(stringToTss, null, 2));


//debugger;

// 447 562
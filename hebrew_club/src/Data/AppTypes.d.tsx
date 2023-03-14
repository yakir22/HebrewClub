export interface INavigation {
	reset: (arg0: { index: number; routes: { name: string; }[]; }) => void;
	navigate: (arg0: string) => void;
}


export interface ITextEntity {
	type: string;
	text: string;
}

export interface ITelegramTextEntry {
	type: string;
	text: string;
	from_id: string;
	from: string;
	date_unixtime: number;
	date: string;
	id: number;
	text_entities: ITextEntity[];
	file?: string;
	media_type?: string;
	mime_type?: string;
	duration_seconds?: number,

}

export interface IQuestion {
	id?: number;
	title: string;
	sound?: string;
}

export interface IWord {
	id?: number;
	text: string;
	sound?: string;
	translation?: string;
}

export interface IExercise {
	id?: string;
	title?: string;
	questions?: IQuestion[];
	words?: IWord[];
}



export interface IOneDayQuestions {
	t1: string[];
	t2: string[][];
	otherMessages: ITelegramTextEntry[];
}
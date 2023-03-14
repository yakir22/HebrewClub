import { makeAutoObservable, makeObservable, action, computed, observable } from 'mobx';
import { createContext } from 'react';
import { IExercise, ITelegramTextEntry } from './AppTypes.d';

class MainStore {
	private _me: any = undefined;
	public get me(): any {
		return this._me;
	}
	public set me(value: any) {
		this._me = value;
	}

	private _accessToken: string = '';
	public get accessToken(): string {
		return this._accessToken;
	}
	public set accessToken(value: string) {
		this._accessToken = value;
	}

	private _refreshToken: string = '';
	public get refreshToken(): string {
		return this._refreshToken;
	}
	public set refreshToken(value: string) {
		this._refreshToken = value;
	}

	private _error: string = '';
	public get error(): string {
		return this._error;
	}
	public set error(value: string) {
		this._error = value;
	}

	private _telegramTextEntries: ITelegramTextEntry[] = [];
	public get telegramTextEntries(): ITelegramTextEntry[] {
		return this._telegramTextEntries;
	}
	public set telegramTextEntries(value: ITelegramTextEntry[]) {
		this._telegramTextEntries = value;
	}


	private _excercise: IExercise = {};
	public get excercise(): IExercise {
		return this._excercise;
	}
	public setExcercise(value: IExercise) {
		this._excercise = value;
	}
	private _quesionId: number = -1;
	public get quesionId(): number {
		return this._quesionId;
	}
	setQuesionId(id: number) {
		this._quesionId = id;
	}

	constructor() {
		makeAutoObservable(this);
	}
}


const __mainStore = new MainStore();
const __mainStoreContext = createContext(__mainStore);
const getMainStoreContext = () => __mainStoreContext;

export const getMainStore = () => __mainStore;
export default getMainStoreContext;
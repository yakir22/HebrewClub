import React, { useContext, useEffect } from 'react';
import { ScrollView, StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import Sound from 'react-native-sound';
import RNFetchBlob from "rn-fetch-blob";
import { unzip } from 'react-native-zip-archive';
import { INavigation, ITextEntity } from '../Data/AppTypes.d';
import getMainStoreContext from '../Data/MainStore';
import { useMainStore } from '../Data/MisckHooks';
// @ts-ignore
import md5 from 'md5';
import { observer } from 'mobx-react-lite';

const downloadAndExtractZip = async (exercise: string) => {
	const url = `https://www.amirelkayam.com/hc/${exercise}.zip`;
	console.log('url:', url);
	// const localFilePath = `${RNFetchBlob.fs.dirs.DocumentDir}/sounds.zip`;
	let localFilePath;
	const extractedPath = `${RNFetchBlob.fs.dirs.CacheDir}/exercises`;

	// Download the zip file
	await RNFetchBlob.config({ fileCache: true })
		.fetch('GET', url)
		.then((res) => {
			localFilePath = res.path();
		});

	if (localFilePath) {
		console.log('localFilePath:', localFilePath);
		await unzip(localFilePath, extractedPath);
	}

	return `${extractedPath}/${exercise}`;
};

const loadAudioFile = (name: string) => {
	return new Promise<Sound>((resolve, reject) => {
		const sound = new Sound(name, Sound.MAIN_BUNDLE, (error) => {
			if (error) {
				reject(error);
			} else {
				resolve(sound);
			}
		});
	});
};
const playAudioFile = (sound: Sound) => {
	return new Promise<boolean>((resolve, reject) => {
		sound.play((success) => {
			if (success) {
				console.log('successfully finished playing');
				resolve(true);
			} else {
				console.log('playback failed due to audio decoding errors');
				reject(new Error('Error playing audio file.'));
			}
		});
	});
};

async function playAudio(filename: string) {
	try {
		const sound = await loadAudioFile(filename);
		console.log('Audio file loaded successfully!');
		await playAudioFile(sound);
		console.log('Audio file played successfully!');
	} catch (error) {
		console.log('Error:', error);
	}
}

const ThisWeekPage = observer(() => {
	const mainStore = useContext(getMainStoreContext());
	// const [questions, setQuestions] = React.useState<string[]>([]);
	const [extractedPath, setExtractedPath] = React.useState<string | null>(null);
	const [audioFile, setAudioFile] = React.useState<string | null>(null);
	const [title, setTitle] = React.useState<string | null>(null);
	const [subtitle, setSubtitle] = React.useState<string | null>(null);

	const navigation = useNavigation<INavigation>();
	const handlePress = (id: number) => {
		console.log('Button pressed!');
		if (id == -1) {
			playAudio(audioFile!);
			return;
		}
		mainStore.setQuesionId(id);
		navigation.navigate('Answer');
	};

	useEffect(() => {
		async function doit() {
			try {
				const extractedPath = await downloadAndExtractZip('00001');
				setExtractedPath(extractedPath);
			}
			catch (error) {
				console.log('Error:', error);
				setExtractedPath('');
			}
		}
		doit();
	}, []);
	useEffect(() => {
		if (extractedPath == null) {
			return;
		}
		async function doit() {
			try {
				if (extractedPath) {
					const jsonString = await RNFetchBlob.fs.readFile(`${extractedPath}/class.json`, 'utf8');
					const json = JSON.parse(jsonString);
					console.log('audio:', `${extractedPath}/${json[2].file}`);
					setTitle((json[0].text_entities as ITextEntity[]).map((entity) => entity.text).join(''));
					setSubtitle((json[1].text_entities as ITextEntity[]).map((entity) => entity.text).join(''));
					setAudioFile(`${extractedPath}/${json[2].file}`);
					mainStore.telegramTextEntries = json;
					// playAudio(`${extractedPath}/${json[2].file}`);
				}
			} catch (error) {
				console.log('Error:', error);
			}
		}
		doit();
	}, [extractedPath]);

	useEffect(() => {
		// split title by line. each line is a question to be set in a state
		if (!subtitle || !title) {
			return;
		}
		const lines = subtitle.split('\n');
		// find first empty string in array and split array into two arrays
		const index = lines.findIndex((line) => line.trim().length === 0);
		const questions = lines.slice(0, index);
		const words = lines.slice(index + 1);

		console.log('setExcercise:');
		mainStore.setExcercise({
			title,
			questions: questions.map((line, index) => { return { id: index, title: line, sound: md5(title) }; }),
			id: '00001',
			words: words.map((word, index) => { return { id: index, text: word.split('-')[0], sound: md5(word), translation: word.split('-')[1] }; }),
		});
	}, [subtitle, title]);
	return (
		<ScrollView>
			<View style={styles.container}>
				<Text style={styles.title}>{mainStore.excercise.title} </Text>
				{/* <Text style={styles.title}>{subtitle}</Text> */}
				<TouchableOpacity style={styles.button} onPress={() => handlePress(-1)}>
					<Text style={styles.buttonText}>PlaySound</Text>
				</TouchableOpacity>
				{
					mainStore.excercise.questions?.map((question, index) => {
						return (
							<TouchableOpacity style={styles.button} onPress={() => handlePress(index)} key={index}>
								<Text style={styles.buttonText}>{question.title}</Text>
							</TouchableOpacity>
						);
					})
				}
			</View>
		</ScrollView>
	);
});

const styles = StyleSheet.create({
	container: {
		flex: 1,
		alignItems: 'center',
		justifyContent: 'center',
	},
	title: {
		fontSize: 24,
		fontWeight: 'bold',
		marginBottom: 20,
		color: 'red'
	},
	button: {
		backgroundColor: '#e0e0e0',
		paddingVertical: 10,
		paddingHorizontal: 20,
		borderRadius: 5,
		marginVertical: 10,
	},
	buttonText: {
		color: 'black',
		minWidth: 300,
		width: 300,
		maxWidth: 300,
		minHeight: 30,
		height: 30,
		maxHeight: 30,
		fontSize: 16,
		fontWeight: 'bold',
	},
});

export default ThisWeekPage;
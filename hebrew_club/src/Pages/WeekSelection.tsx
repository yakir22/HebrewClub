
import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { View, Text, ScrollView, StyleSheet, Image } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import { INavigation, IOneDayQuestions, ITelegramTextEntry } from '../Data/AppTypes.d';
import { useMainStore } from '../Data/MisckHooks';
const data = require('../Data/groupedExcersizes.json') as IOneDayQuestions[][];


const Ticket: React.FC<{ questions: string[], sentences: string[][], other: ITelegramTextEntry[] }> = ({ questions, sentences, other }) => {
	const mainStore = useMainStore();
	const navigation = useNavigation<INavigation>();
	function handlePress() {
		mainStore.telegramTextEntries = other.slice(0, 10);
		console.log('other', mainStore.telegramTextEntries.length)
		mainStore.setExcercise({
			questions: questions.map((q, index) => ({ title: q })),
			words: sentences.map((s, index) => ({ text: s[0], translation: s[1] }))
		});
		navigation.navigate('Answer');
	}

	return <>
		<TouchableOpacity onPress={() => handlePress()}>
			<View style={styles.questionContainer}>
				<Text style={styles.questionText}>{questions[0]}</Text>
			</View>
		</TouchableOpacity>
	</>
}
const WeekSelection = () => {
	return <View style={styles.pageContainer}>
		<View style={styles.pageTitleContainer}>
			<Text style={styles.pageTitle}>Выберите тему </Text>
		</View>
		<ScrollView style={{ height: '80%' }}>
			{
				data.map((week, index) => {
					if (week.length < 1) return null;
					return <React.Fragment key={`sv${index}`}>
						<View style={styles.weekTitle}>
							<Image source={require('../assets/pigi.png')} />
							<Text style={styles.weekTitleText}>חברים</Text>
						</View>
						<View style={styles.weekContainer} >
							<ScrollView style={styles.maskOut} horizontal={true} >
								{week.map((day, index) => (
									<Ticket key={`day${index}`} questions={day.t1} sentences={day.t2} other={day.otherMessages} />
								))}
							</ScrollView>
						</View>
					</React.Fragment>
				})
			}
		</ScrollView>
	</View>
}


const styles = StyleSheet.create({
	pageContainer: {
		backgroundColor: '#FAF5F3'
	},
	pageTitleContainer: {
		padding: 50,
		width: '100%',
		height: '20%',
		justifyContent: 'center',
		alignItems: 'center',
	},
	pageTitle: {
		color: 'black',
		fontSize: 32,
		fontWeight: 'bold',
	},
	weekTitle: {
		flexDirection: 'row',
		textAlignVertical: 'center',
		alignItems: 'center',
		marginLeft: 10,
	},
	weekTitleText: {
		fontSize: 24,
		fontWeight: 'bold',
		color: '#E1705D',
	},
	maskOut: {
		overflow: 'hidden',
		clipsToBounds: true
	},
	weekContainer: {
		padding: 10,
		margin: 10,
		borderRadius: 30,
		borderColor: 'black',
		borderWidth: 1,
		borderStyle: 'solid',
	},
	questionContainer: {
		height: 120,
		justifyContent: 'center',
		alignItems: 'center',
		backgroundColor: '#fff',
		margin: 20,
		width: 240,
		borderRadius: 30,
		borderColor: 'orange',
		borderWidth: 1,
		borderStyle: 'solid'
	},
	questionText: {
		padding: 10,
		fontSize: 16,
		fontWeight: 'bold',
		color: 'black'
	}

});

export default WeekSelection;
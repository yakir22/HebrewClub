import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, StyleSheet, TouchableOpacity } from 'react-native';
import useFirestoreUser, { useMainStore } from '../Data/MisckHooks';
import firestore from '@react-native-firebase/firestore';
import { useNavigation } from '@react-navigation/native';
import { observer } from 'mobx-react-lite';
import { INavigation } from '../Data/AppTypes.d';


const AnswerPage = observer(() => {
	const mainStore = useMainStore();
	const navigation = useNavigation<INavigation>();

	const user = useFirestoreUser();
	const [text, setText] = useState('');
	const [buttonDisabled, setButtonDisabled] = useState(false);
	const minChars = 5;
	const title = mainStore.excercise.questions!.map(q => q.title).join('\n');
	const handleTextChange = (text: string) => {
		setText(text);
		setButtonDisabled(text.length < minChars);
	};

	const handleSubmit = async () => {
		console.log(`Submitted: ${text}`, user);
		const doc = await firestore()
			.collection('Users').doc(user?.user.id).collection('Answers').
			add({
				question: title,
				answer: text
			});

		(navigation as any).reset({
			index: 0,
			routes: [{ name: 'Summery' }],
		});
	};

	return (
		<View style={styles.container}>
			<Text style={styles.title}>{title}</Text>
			{
				mainStore.excercise.words!.map((word, index) => {
					return <TouchableOpacity onPress={() => setText(text + word.text)} key={index}>
						<Text style={styles.words} key={index}>{word.text}</Text>
					</TouchableOpacity>
				})
			}
			<TextInput
				style={styles.input}
				multiline
				placeholderTextColor='#00FF00' // Green color
				placeholder={`לפחות ${minChars} תווים`}
				value={text}
				onChangeText={handleTextChange}
			/>
			<Button title="Submit" onPress={handleSubmit} disabled={buttonDisabled} />
			<Button title="Read Other" onPress={() => navigation.navigate('Chat')} disabled={buttonDisabled} />
		</View>
	);
});

const styles = StyleSheet.create({
	container: {
		flex: 1,
		padding: 20,
	},
	words: {
		fontSize: 14,
		backgroundColor: 'yellow',
		// maxWidth: 300,
		borderRadius: 10,
		width: 200,
		marginBottom: 10,
		textAlign: 'center',
		color: 'red'
	},
	title: {
		fontSize: 24,
		fontWeight: 'bold',
		marginBottom: 20,
		color: 'red'

	},
	input: {
		textAlignVertical: 'top',
		color: 'magenta',
		height: 200,
		borderWidth: 1,
		borderColor: '#ccc',
		padding: 10,
		marginBottom: 20,
	},
});

export default AnswerPage;

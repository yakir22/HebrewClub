import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import useFirestoreUser from './MisckHooks';
import firestore from '@react-native-firebase/firestore';
import { useNavigation } from '@react-navigation/native';


const AnswerPage = () => {
	const navigation = useNavigation();

	const user = useFirestoreUser();
	const [text, setText] = useState('');
	const [buttonDisabled, setButtonDisabled] = useState(true);
	const minChars = 5;
	const handleTextChange = (text: string) => {
		setText(text);
		setButtonDisabled(text.length < minChars);
	};

	const handleSubmit = async () => {
		console.log(`Submitted: ${text}`, user);
		const doc = await firestore()
			.collection('Users').doc(user?.user.id).collection('Answers').
			add({
				question: 'האם יש לך חולה בבית?',
				answer: text
			});

		(navigation as any).reset({
			index: 0,
			routes: [{ name: 'Summery' }],
		});
	};

	return (
		<View style={styles.container}>
			<Text style={styles.title}>My Page</Text>
			<TextInput
				style={styles.input}
				multiline
				placeholderTextColor='#00FF00' // Green color
				placeholder={`לפחות ${minChars} תווים`}
				value={text}
				onChangeText={handleTextChange}
			/>
			<Button title="Submit" onPress={handleSubmit} disabled={buttonDisabled} />
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		padding: 20,
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

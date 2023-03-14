import { useNavigation } from '@react-navigation/native';
import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';
import ConfettiCannon from 'react-native-confetti-cannon';
import { INavigation } from '../Data/AppTypes.d';
import { useScreenSize } from '../Data/MisckHooks';

const SummeryPage = () => {
	const size = useScreenSize();
	const navigation = useNavigation<INavigation>();

	const handleReadOther = () => {
		navigation.navigate('Chat');
	};

	const handleNextQuestion = () => {
		navigation.navigate('Answer');
	};

	const handleBackToMain = () => {
		navigation.reset(
			{
				index: 0,
				routes: [{ name: 'WeekSelection' }],
			}
		);
	};

	return (
		<View style={styles.container}>
			<ConfettiCannon origin={{ x: size.width / 2, y: size.height / 2 }} count={200} explosionSpeed={1000} fallSpeed={3000} />
			{/* <Image source={require('./confetti.png')} style={styles.confetti} /> */}
			<Text style={styles.title}>Congratulations!</Text>
			<View style={styles.buttonContainer}>
				<TouchableOpacity style={styles.button} onPress={handleReadOther}>
					<Text style={styles.buttonText}>Read Other</Text>
				</TouchableOpacity>
				<TouchableOpacity style={styles.button} onPress={handleNextQuestion}>
					<Text style={styles.buttonText}>Next Question</Text>
				</TouchableOpacity>
				<TouchableOpacity style={styles.button} onPress={handleBackToMain}>
					<Text style={styles.buttonText}>Back to Main</Text>
				</TouchableOpacity>
			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: 'center',
		alignItems: 'center',
	},
	confetti: {
		position: 'absolute',
		top: 0,
		left: 0,
		right: 0,
		bottom: 0,
		zIndex: -1,
	},
	title: {
		fontSize: 36,
		fontWeight: 'bold',
		marginBottom: 50,
	},
	buttonContainer: {
		flexDirection: 'column',
		alignItems: 'center',
	},
	button: {
		backgroundColor: 'green',
		width: 300,
		height: 30,
		borderRadius: 5,
		marginBottom: 10,
		justifyContent: 'center',
		alignItems: 'center',
	},
	buttonText: {
		color: 'white',
		fontSize: 16,
		fontWeight: 'bold',
	},
});

export default SummeryPage;

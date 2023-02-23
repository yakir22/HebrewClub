import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';





const ThisWeekPage = () => {
	const navigation = useNavigation();
	const handlePress = (id: number) => {
		console.log('Button pressed!');
		(navigation as any).navigate('Answer');
	};
	return (
		<View style={styles.container}>
			<Text style={styles.title}>This week topic : Music</Text>
			<TouchableOpacity style={styles.button} onPress={() => handlePress(0)}>
				<Text style={styles.buttonText}>Do you think that music is important?</Text>
			</TouchableOpacity>
			<TouchableOpacity style={styles.button} onPress={() => handlePress(1)}>
				<Text style={styles.buttonText}>Do you like music?</Text>
			</TouchableOpacity>
			<TouchableOpacity style={styles.button} onPress={() => handlePress(2)}>
				<Text style={styles.buttonText}>What music do you like?</Text>
			</TouchableOpacity>
			<TouchableOpacity style={styles.button} onPress={() => handlePress(3)}>
				<Text style={styles.buttonText}>Why music is so popular?</Text>
			</TouchableOpacity>
		</View>
	);
};

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
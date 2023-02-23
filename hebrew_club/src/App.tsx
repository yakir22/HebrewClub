import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createStackNavigator } from '@react-navigation/stack';
import SignInPage from './SigninPage';
import ThisWeekPage from './ThisWeekPage';
import ChatPage from './ChatPage';
import AnswerPage from './AnswerPage';
import SummeryPage from './SummeryPage';


const Stack = createStackNavigator();
const App = () => (
	<NavigationContainer>
		<Stack.Navigator>
			<Stack.Screen name="Signin" component={SignInPage} />
			<Stack.Screen name="ThisWeek" component={ThisWeekPage} />
			<Stack.Screen name="Chat" component={ChatPage} />
			<Stack.Screen name="Answer" component={AnswerPage} />
			<Stack.Screen name="Summery" component={SummeryPage} />
		</Stack.Navigator>
	</NavigationContainer>
);

export default App;

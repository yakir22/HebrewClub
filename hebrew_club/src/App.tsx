import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createStackNavigator } from '@react-navigation/stack';
import SignInPage from './Pages/SigninPage';
import ThisWeekPage from './Pages/ThisWeekPage';
import WeekSelection from './Pages/WeekSelection';
import ChatPage from './Pages/ChatPage';
import AnswerPage from './Pages/AnswerPage';
import SummeryPage from './Pages/SummeryPage';


const Stack = createStackNavigator();
const App = () => (
	<NavigationContainer>
		<Stack.Navigator>
			<Stack.Screen name="Signin" component={SignInPage} />
			<Stack.Screen name="WeekSelection" component={WeekSelection} />
			<Stack.Screen name="ThisWeek" component={ThisWeekPage} />
			<Stack.Screen name="Chat" component={ChatPage} />
			<Stack.Screen name="Answer" component={AnswerPage} />
			<Stack.Screen name="Summery" component={SummeryPage} />
		</Stack.Navigator>
	</NavigationContainer>
);

export default App;

import { GoogleSignin } from '@react-native-google-signin/google-signin';
import { Button, Text, View } from 'react-native'
import auth from '@react-native-firebase/auth';
import AsyncStorage from '@react-native-async-storage/async-storage';
import firestore from '@react-native-firebase/firestore';
import { useEffect, useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import { INavigation } from '../Data/AppTypes.d';

// let app;
// if (firebase.apps.length === 0) {
// 	app = firebase.initializeApp(firebaseConfig);
// } else {
// app = firebase.app()
// }

GoogleSignin.configure({
	webClientId: '160331476715-9nq0h9j41jnhtdk2l4cp77ljkjuvomhn.apps.googleusercontent.com',
});


async function onSignIn() {
	const tokens = await GoogleSignin.getTokens();
	await AsyncStorage.setItem('userCredentials', JSON.stringify(tokens));
}

// When the app is launched
async function checkSignInStatus() {
	const credentialsJson = await AsyncStorage.getItem('userCredentials');
	if (credentialsJson) {
		const credentials = JSON.parse(credentialsJson);
		const now = new Date().getTime();
		if (credentials.accessTokenExpirationDate > now) {
			return await GoogleSignin.signInSilently();
		} else {
			const { refreshToken } = credentials;
			const { accessToken } = await GoogleSignin.getTokens();
			credentials.accessToken = accessToken;
			credentials.accessTokenExpirationDate =
				new Date().getTime() + credentials.accessTokenExpirationTime;
			await AsyncStorage.setItem('userCredentials', JSON.stringify(credentials));
			return await GoogleSignin.signInSilently();
		}
	}
}

const onGoogleButtonPress = async () => {
	try {
		await GoogleSignin.hasPlayServices();
		const { idToken } = await GoogleSignin.signIn();
		const googleCredential = auth.GoogleAuthProvider.credential(idToken);
		const userInfo = await GoogleSignin.getCurrentUser();
		await onSignIn();
		if (userInfo) {
			const doc = await firestore()
				.collection('Users').doc(userInfo.user.id).
				set({
					name: 'Ada Lovelace',
					age: 30,
				});
			console.log('doc', userInfo.user.id);
		}
		return userInfo;

	} catch (error) {
		console.error(error);
	}
	return null;
};



const SignInPage = () => {
	const navigation = useNavigation<INavigation>();
	const [user, setUser] = useState<any>(null);
	useEffect(() => {
		async function checkUser() {
			const user = await checkSignInStatus();
			setUser(user);
		}
		checkUser();
	}, []);
	useEffect(() => {
		if (user) {
			navigation.reset({
				index: 0,
				routes: [{ name: 'ThisWeek' }],
			});
		}
	}, [user]);

	console.log('user', user);
	return <>
		{
			!user && <Button title="Sign in with Google" onPress={async () => setUser(await onGoogleButtonPress())} />
		}
		{/* {
			user && <ThisWeekPage />
		} */}
	</>
}


export default SignInPage;

import { useContext, useEffect, useState } from 'react';
import auth from '@react-native-firebase/auth';
import firestore from '@react-native-firebase/firestore';
import { GoogleSignin, User } from '@react-native-google-signin/google-signin';
import { Dimensions } from 'react-native';
import getMainStoreContext from './MainStore';

export const useScreenSize = () => {
	const [screenSize, setScreenSize] = useState(Dimensions.get('window'));

	useEffect(() => {
		return () => {
		};
	}, []);

	return screenSize;
};
export const useMainStore = () => {
	const mainStore = useContext(getMainStoreContext());;
	return mainStore;
};



const useFirestoreUser = () => {
	const [user, setUser] = useState<User | null>(null);

	useEffect(() => {
		const fetchUser = async () => {
			try {
				// Get the current user from Google Sign-In
				const currentUser = await GoogleSignin.getCurrentUser();

				if (currentUser) {
					setUser(currentUser);
					// // Check if the user is already in Firestore
					// const userRef = firestore().collection('users').doc(currentUser.user.id);
					// const snapshot = await userRef.get();

					// if (snapshot.exists) {
					// 	// If the user is already in Firestore, update the local user state
					// 	setUser(snapshot.data());
					// } else {
					// 	// If the user is not in Firestore, create a new document for the user
					// 	const userData = {
					// 		id: currentUser.user.id,
					// 		name: currentUser.user.name,
					// 		email: currentUser.user.email,
					// 		photoUrl: currentUser.user.photo,
					// 	};
					// 	await userRef.set(userData);
					// 	setUser(userData);
					// }
				} else {
					setUser(null);
				}
			} catch (error) {
				console.error(error);
			}
		};

		const unsubscribe = auth().onAuthStateChanged(() => {
			fetchUser();
		});

		return () => {
			unsubscribe();
		};
	}, []);

	return user;
};

export default useFirestoreUser;

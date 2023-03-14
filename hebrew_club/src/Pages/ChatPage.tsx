import React, { useEffect } from 'react';
import { StyleSheet, View, Text, ScrollView, TouchableOpacity, Alert } from 'react-native';
import { useMainStore } from '../Data/MisckHooks';
import { observer } from 'mobx-react-lite';
import { TouchableHighlight } from 'react-native-gesture-handler';
const ChatBubble: React.FC<{ message: string, isMe: boolean, messageId: number, deleteEntry: (id: number) => void }> = ({ message, isMe, messageId, deleteEntry: fetchData }) => {
	const mainStore = useMainStore();
	const bubbleStyles = [
		styles.bubble,
		isMe ? styles.bubbleRight : styles.bubbleLeft,
	];
	const textStyles = [
		styles.message,
		isMe ? styles.messageRight : styles.messageLeft,
	];

	const deleteIt = () => {
		if (mainStore.me.user.email !== 'yakir22@gmail.com') {
			return;
		}
		Alert.alert(
			'Are you sure?',
			'Do you really want to delete?',
			[
				{
					text: 'Cancel',
					onPress: async () => { },
					style: 'cancel',
				},
				{
					text: 'OK',
					onPress: () => {
						fetchData(messageId);
					},
				},
			],
			{ cancelable: false },
		);
	};
	return (
		<TouchableOpacity onPress={deleteIt}>
			<View style={bubbleStyles}>
				<Text style={textStyles}>{message}</Text>
			</View>
		</TouchableOpacity>
	);
};

const ChatPage = observer(() => {
	const mainStore = useMainStore();
	const [deleted, setDeleted] = React.useState<string[]>([]);
	async function deleteEntry(id?: number) {
		try {
			const response = await fetch('https://yakirelkayam.com/HebrewClub/delete.php' + (id ? '?id=' + id : ''));
			setDeleted(await response.json());
		} catch (err) {
			console.log(err);
		}
	}

	useEffect(() => {
		deleteEntry();
	}, []);

	// console.log('Deleted', deleted.includes("199"), deleted, mainStore.telegramTextEntries.filter((entry => !deleted.includes(entry.id.toString()))).map((entry, index) => entry.id));

	if (!mainStore.telegramTextEntries) {
		return <View style={styles.container}>
			<Text>no data</Text>
		</View>
	}
	return (
		<ScrollView>
			<View style={styles.container}>
				{
					mainStore.telegramTextEntries.filter((entry => !deleted.includes(entry.id.toString()))).map((entry, index) => {
						return <ChatBubble deleteEntry={deleteEntry} message={entry.text} isMe={index % 2 > 0} key={index} messageId={entry.id} />
					})
				}
			</View>
		</ScrollView>
	);
});

const styles = StyleSheet.create({
	container: {
		flex: 1,
		padding: 10,
		backgroundColor: '#f5f5f5',
	},
	bubble: {
		backgroundColor: '#fff',
		padding: 10,
		borderRadius: 10,
		maxWidth: '80%',
		marginBottom: 10,
	},
	bubbleLeft: {
		alignSelf: 'flex-start',
		marginLeft: 10,
	},
	bubbleRight: {
		alignSelf: 'flex-end',
		marginRight: 10,
		backgroundColor: '#dcf8c6',
	},
	message: {
		fontSize: 16,
		lineHeight: 20,
	},
	messageLeft: {
		color: '#000',
	},
	messageRight: {
		color: '#000',
	},
});

export default ChatPage;

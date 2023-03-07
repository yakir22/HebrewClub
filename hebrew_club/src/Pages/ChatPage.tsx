import React from 'react';
import { StyleSheet, View, Text, ScrollView } from 'react-native';
import { useAppStore } from '../Data/MisckHooks';
import { observer } from 'mobx-react-lite';
const ChatBubble: React.FC<{ message: string, isMe: boolean }> = ({ message, isMe }) => {
	const bubbleStyles = [
		styles.bubble,
		isMe ? styles.bubbleRight : styles.bubbleLeft,
	];
	const textStyles = [
		styles.message,
		isMe ? styles.messageRight : styles.messageLeft,
	];

	return (
		<View style={bubbleStyles}>
			<Text style={textStyles}>{message}</Text>
		</View>
	);
};

const ChatPage = observer(() => {
	const appStore = useAppStore();

	console.log('ChatPage', appStore.telegramTextEntries.length);
	return (
		<ScrollView>
			<View style={styles.container}>
				{
					appStore.telegramTextEntries.map((entry, index) => {
						return <ChatBubble message={entry.text_entities.map((e) => e.text).join(' ')} isMe={entry.from === 'Ali'} key={index} />
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

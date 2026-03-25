import { View, TextInput, Button, ScrollView, Text } from 'react-native';
import { intelliflow } from '@intelliflow/crm-mobile-sdk';
import { useState } from 'react';
import * as Speech from 'expo-speech';

export default function AskAIScreen() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const ask = async () => {
    const res = await intelliflow.askAI(query);
    setResponse(res.answer);
    Speech.speak(res.answer);
  };

  return (
    <View className="flex-1 p-4">
      <Text className="text-2xl font-bold">Ask AI (Voice Enabled)</Text>
      <TextInput placeholder="Ask anything (e.g. Show this month's revenue)" value={query} onChangeText={setQuery} className="border p-2 my-4" />
      <Button title="Send (Voice + Text)" onPress={ask} />
      <ScrollView className="mt-6"><Text>{response}</Text></ScrollView>
    </View>
  );
}
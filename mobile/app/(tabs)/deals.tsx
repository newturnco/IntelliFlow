import { View, Text } from 'react-native';
import { intelliflow } from '@intelliflow/crm-mobile-sdk';
import { useEffect, useState } from 'react';

export default function DealsScreen() {
  const [pipeline, setPipeline] = useState<any>(null);

  useEffect(() => {
    intelliflow.getPipeline().then(setPipeline);
  }, []);

  return (
    <View className="flex-1 p-4">
      <Text className="text-2xl font-bold">Pipeline Forecast</Text>
      {pipeline && <Text>Forecast: ${pipeline.forecast} | Won: ${pipeline.total_revenue}</Text>}
    </View>
  );
}
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import HomeScreen from './Home'  //marca, nome e botões "VER PROVAS" "SAIR" 
import MaratonaListScreen from './MaratonaList' //lista com todas as maratonas e botão "VER FAVORITOS"
import MaratonaDetailsScreen from './MaratonaDetails' //detalhes de uma prova (site para comprar ingressos, coordenadas)

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
    <Stack.Navigator initialRouteName="Home">
    <Stack.Screen name="Home" component={HomeScreen} />
    <Stack.Screen name="MaratonaList" component={MaratonaListScreen} />
    <Stack.Screen name="MaratonaDetails" component={MaratonaDetailsScreen} />
     </Stack.Navigator>
    </NavigationContainer>
  );
}
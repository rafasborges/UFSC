import * as React from 'react';
import { View, Text, Image, Button, StyleSheet, BackHandler } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.containerFundo}>
      <View style={styles.container}>
        <Image style={styles.logo} source={require('./assets/contact.png')} />
        <Text style={styles.title} >Meus Contatos</Text>
      </View>
      <View style={styles.button}>
        <Button title="Ver Contatos" onPress={() => navigation.navigate('ContactList')} />
      </View>
      <View style={styles.button}>
        <Button title="Sair" onPress={() => BackHandler.exitApp() } />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 60,
  },
  containerFundo:{
    backgroundColor: 'white',
    flex: 1,
  },
  logo: {
    height: 160,
    width: 160,
  },
  title: {
    padding: 30,
    fontSize: 30,
  },
  button: {
    backgroundColor: '#add8e6', // Azul Bebê
    paddingVertical: 20,
    paddingHorizontal: 50,
    borderRadius: 20,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 80,
    marginRight: 80,
    marginBottom:20,
  }
  
});

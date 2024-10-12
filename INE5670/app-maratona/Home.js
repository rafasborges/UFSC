import * as React from 'react';
import { View, Text, Image, TouchableOpacity, Linking, StyleSheet, BackHandler, Button } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.containerFundo}>

      <View style={styles.container}>
        <Image style={styles.logo} source={require('./assets/man-40739.png')} />
        <Text style={styles.title} >Nonstop Running</Text>
      </View>

      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('MaratonaList')}>
        <Text style={styles.buttonText}>Ver Provas</Text>
      </TouchableOpacity>
    
      <TouchableOpacity style={styles.button} onPress={() => Linking.openURL("https://www.instagram.com/isisbertoldi?igsh=MW9jd29landkZGdi")}>
        <Text style={styles.buttonText}>Inspiração para correr!</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button} onPress={() => Linking.openURL("https://youtu.be/acCZb8Ee0k8?si=uSzonV_EejT-A1B1")}>
        <Text style={styles.buttonText}>Preparação Maratona</Text>
      </TouchableOpacity>
      
    </View>
  );
}

const styles = StyleSheet.create({
  containerFundo:{
    backgroundColor: '#rgba(140, 11, 224, 0.2)',
    flex: 1,
  },
  container: {
    alignItems: 'center',
    padding: 60,
  },
  logo: {
    width: 180,
    height:180,
  },
  title: {
    textAlign: 'center',
    display: "flex",    
    padding: 10,
    fontSize: 24,
    fontWeight:"bold",
  },
  button: {
    backgroundColor: 'purple', // Azul Bebê
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 30,
    alignItems: 'center',
    marginLeft: 80,
    marginRight: 80,
    marginBottom:15,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  }
});

import * as React from 'react';
import { Text, View, StyleSheet, Button, Linking, Image, TouchableOpacity } from 'react-native';
import { Platform } from 'react-native';


export default function MaratonaDetailsScreen ({ route, navigation }) {
  const {data} = route.params;
  return (
    <View style={styles.containerFundo}>
    {(
      <><View style={styles.container}>
          <Text style={styles.maratonaName}>{data.name}</Text>
          <Image style={styles.image} source={{uri: data.image.toString()}}/>
          <Text style={styles.maratonaDetails}>Cidade: {data.cidade}</Text>
          <Text style={styles.maratonaDetails}>Data: {data.data}</Text>
        </View>
        
        <TouchableOpacity style={styles.button} onPress={() => Linking.openURL(`${data.website}`)}>
          <Text style={styles.buttonText}>Ingressos</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.button} onPress={() => Linking.openURL(`${data.mapa}`)}>
          <Text style={styles.buttonText}>Localização</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button} onPress={() => Linking.openURL(`${data.video}`)}>
          <Text style={styles.buttonText}>Vídeo do evento</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('MaratonaList')}>
          <Text style={styles.buttonText}>Voltar</Text>
        </TouchableOpacity></>
    )}
    </View>
      
  );
}
const styles = StyleSheet.create({
  containerFundo:{
    backgroundColor: '#rgba(140, 11, 224, 0.2)',
    flex: 1,
  },
  container: {
    padding: 15,
  },
  maratonaName: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  maratonaDetails: {
    fontSize: 16,
    marginBottom: 18,
  },
  button: {
    backgroundColor: 'purple', // Azul Bebê
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 30,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 80,
    marginRight: 80,
    marginBottom:20,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  },
  image:{
    resizeMode:'stretch',
    width: 300,
    height: 110,
    alignSelf: 'center',
    //borderTopRightRadius:20,
    //borderTopLeftRadius:20,
    marginBottom: 20
  }
});
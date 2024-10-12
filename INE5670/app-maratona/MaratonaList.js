import React, { useState, useEffect } from 'react';
import { Text, View, StyleSheet, Button, ActivityIndicator, Image, ScrollView, FlatList, TouchableOpacity } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const dataJson = require('./dadosCorridas.json');

export default function MaratonaListScreen({ navigation }) {
  const [favoritos, setFavoritos] = useState([]);
  const [showFavoritos, setShowFavoritos] = useState(false);

  function favoritar(item) {
    favoritos.includes(item) ? ( // testa se a lista de favoritos possui ou não aquele item
      setFavoritos(favoritos.filter(favs => favs != item)) // exclui item dos favoritos
    ) : (
      setFavoritos((array) => [...array, item]) // adiciona item aos favoritos
    )
  }

  return (
    // linha 19: true -> mostra lista com apenas os fav, false -> mostra lista com todas as maratonas
    showFavoritos ? ( 
      // linha 21: lista com + de 1 item -> mostra itens, lista vazia -> mostra msg 'sem fav salvos'
      favoritos.length ? ( // mostra lista com as maratonas salvas
        <ScrollView style={styles.containerFundo}>
          <View style={styles.container}>
            <FlatList
              data={favoritos}
              renderItem={({ item }) => (
                <View>
                  <TouchableOpacity onPress={() => navigation.navigate('MaratonaDetails', { data: item })}>
                    <View style={styles.card}>
                      <Image style={styles.image} source={{ uri: item.image.toString() }} />
                      <Text style={styles.titulos}>{item.name}</Text>
                      <Text style={styles.maratonas}>Cidade: {item.cidade}</Text>
                      <Text style={styles.data}>Data: {item.data}</Text>

                    <TouchableOpacity onPress={() => favoritar(item)}>
                      <Image style={styles.fav} source={require('./assets/iconeCoraPren.jpeg')} />
                    </TouchableOpacity>

                    </View>
                  </TouchableOpacity>
                </View>
              )}
              keyExtractor={(item, index) => index.toString()}
            />
            <TouchableOpacity style={styles.button} onPress={() => setShowFavoritos(!showFavoritos)}>
              <Text style={styles.buttonText}>Voltar</Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
      ) : ( // o que fará caso a lista de favoritos esteja vazia
        <View style={styles.containerFundo}>
          <Text style={styles.semFavMsg}>Sem favoritos salvos</Text>
          <TouchableOpacity style={styles.button} onPress={() => setShowFavoritos(!showFavoritos)}>
            <Text style={styles.buttonText}>Voltar</Text>
          </TouchableOpacity>
        </View>
      )
    ) : ( // mostra a lista com todas as maratonas
      <ScrollView style={styles.containerFundo}>
        <TouchableOpacity style={styles.button} onPress={() => setShowFavoritos(!showFavoritos)}>
          <Text style={styles.buttonText}>Ver Favoritos</Text>
        </TouchableOpacity>

        <View style={styles.container}>
          <FlatList
            data={dataJson}
            renderItem={({ item }) => (
              <View>
                <TouchableOpacity onPress={() => navigation.navigate('MaratonaDetails', { data: item })}>
                  <View style={styles.card}>
                    <Image style={styles.image} source={{ uri: item.image.toString() }} />
                    <Text style={styles.titulos}>{item.name}</Text>
                    <Text style={styles.maratonas}>Cidade: {item.cidade}</Text>
                    <Text style={styles.data}>Data: {item.data}</Text>

                    <TouchableOpacity onPress={() => favoritar(item)} style={styles.fav} >
                      {favoritos.includes(item) ? (
                        <Image style={styles.fav} source={require('./assets/iconeCoraPren.jpeg')} />
                      ) : (
                        <Image style={styles.fav} source={require('./assets/iconeCoraVaza.jpeg')} />
                      )}
                    </TouchableOpacity>
                  </View>
                </TouchableOpacity>
              </View>
            )}
            keyExtractor={(item, index) => index.toString()}
          />

          <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Home')}>
            <Text style={styles.buttonText}>Voltar</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    )
  );
}

const styles = StyleSheet.create({
  containerFundo: {
    backgroundColor: 'rgba(140, 11, 224, 0.2)',
    flex: 1,
  },
  container: {
    padding: 20
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 30,
    paddingBottom: 15,
    marginBottom: 20,
  },
  image: {
    width: '100%',
    height: 130,
    alignSelf: 'center',
    borderTopRightRadius: 30,
    borderTopLeftRadius: 30,
  },
  titulos: {
    paddingHorizontal: 10,
    paddingBottom: 5,
    paddingTop: 10,
    fontSize: 18,
    fontWeight: "bold"
  },
  maratonas: {
    paddingHorizontal: 10,
    paddingTop: 5,
    fontSize: 15,
  },
  data: {
    paddingHorizontal: 10,
    paddingTop: 5,
    fontSize: 15,
  },
  fav: {
    height: 22.6,
    width: 26.64,
    alignSelf: 'flex-end',
    marginRight: 7,
  },
  button: {
    backgroundColor: 'purple',
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 30,
    alignItems: 'center',
    marginHorizontal: 80,
    marginVertical: 20,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  },
  semFavMsg: {
    textAlign: 'center',
    fontSize: 18,
    marginVertical: 30,
  }
});

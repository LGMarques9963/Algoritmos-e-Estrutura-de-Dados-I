#include <iostream>
#include "Pilha.h"

Pilha::Pilha( int size ) {
  elem = new int[size];
  tam = size;
  usados = 0;
}

Pilha::~Pilha( ) {
  delete [] elem;
}

int Pilha::isEmpty( ) {
  return usados == 0;
}

using namespace std;

void Pilha::push( int n ) {
  if ( usados < tam )
    elem[usados++] = n;
  else 
    cout << "Pilha cheia!" << endl;
}

int Pilha::pop( ) {
  if ( ! isEmpty() )
    return elem[--usados];
  else 
    cout << "Pilha vazia!" << endl;
  return -1;
}

void Pilha::print( ) {

  if ( isEmpty() ) return;
  int val = pop();
  cout << "  " << val << endl;
  print();
  push( val );

}

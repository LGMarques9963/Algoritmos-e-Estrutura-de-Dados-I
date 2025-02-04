#include <iostream>
#include "Pilha.h"

using namespace std;

int main( ) {

  Pilha p( 30 );

  while ( 1 > 0 ) {

    char op;
    cout << "Entre seu comando [ipdt+-*/q] : ";
    cin >> op;

    int val, v1, v2;

    switch ( op ) {
      case 'i' :
        cin >> val;
        p.push( val );
        break;
      case 'p' :
        val = p.pop( );
        cout << val << endl;
        break;
      case 'd':
        val = p.pop( );
        p.push( val );
        p.push( val );
        break;
      case 't':
        v1 = p.pop( );
        v2 = p.pop( );
        p.push( v1 );
        p.push( v2 );
        break;

      case '+' : p.push( p.pop() + p.pop() ); break;
      case '-' : p.push( p.pop() - p.pop() ); break;
      case '*' : p.push( p.pop() * p.pop() ); break;
      case '/' : p.push( p.pop() / p.pop() ); break;
      case 'q' : return 0;
    }

    cout << endl;
    p.print();
    cout << endl;

  }

}

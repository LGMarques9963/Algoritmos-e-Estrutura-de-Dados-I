
class Pilha {

  private:
  int *elem;
  int tam, usados;

  public:

  Pilha( int );
  ~Pilha( );

  void push( int );
  int pop( );
  int isEmpty();

  void print( );
};

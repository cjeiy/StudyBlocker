#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main(void)
{
    string line;
    fstream f ("C:\Windows\System32\drivers\etc\hosts");

    if ( f.is_open() )
    {
        while ( f.good() )
        {

            getline(f,line);
            cout << line << endl;
        }

        f.close();
    } else
        cout << "Error" << endl;

    system("pause");

    return 0;
}
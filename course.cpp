#include <iostream>
#include <cmath>
using namespace std;
class math{
public:
string math="676767这是你的分数";
virtual void fenshu(){}
};
class student:math{
public:
void fenshu()override{
    cout<<"very good"<<endl;
};
};
int main(){
math goo;
student good;
good.fenshu();
cout<<"可能会有一些bug"<<endl;
cout<<"欢迎使用多功能计算器输入exit退出"<<endl;
while(true){
double  num;
    double  numb;
    cout<<goo.math<<endl;
    cout<<"请输入任意一个数字"<<endl;
    cin>>num;
string exit;
cin>>exit;
if(exit=="exit"){
    break;
}
while ( !(cin >> num) )
{
    cin.clear();
    cin.ignore(1024, '\n');
    cout << "输入无效，请重新输入数字：" << endl;
}
    cout<<"请输入第二个数字，这是为了更多运算方式"<<endl;
    cin>>numb;
while(!(cin>>numb))
{
    cin.clear();
    cin.ignore(1024,'\n');
    cout<<"输入无效，请重新输入数字："<<endl;
}
    cout<<"平方根"<<sqrt(num)<<endl;
    cout<<"幂运算"<<pow(num,numb)<<endl;    
    return  0;
}
}


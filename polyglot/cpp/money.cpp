#include <vector>
struct Transaction{double amount;bool income;};
double balance(const std::vector<Transaction>&v){double b=0;for(auto&t:v)b+=t.income?t.amount:-t.amount;return b;}

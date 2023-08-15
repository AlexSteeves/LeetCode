class Solution {
    public double myPow(double x, int n) {
        if(n == 0){
            return 1;
        }
        if(n < 0){
            x = 1/x;

            if (n == Integer.MIN_VALUE) {
                n++; // Avoid overflow when negating
                return x * myPow(x, -n);
            }

            n = -n;
        }
        
        

        double result = 1.0;
        double current = x;
        

        while(n > 0){
            if (n % 2 == 1){
                result*= current;
            }
            current *=current;
            n /= 2;

        }
        return result;
    }
}
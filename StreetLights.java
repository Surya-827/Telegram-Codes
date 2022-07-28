public int coverage(int input1, int [][] input2)

        {

                int sum = input2[0][1] - input2[0][0];

                int max = input2[0][1];

                for(int i=1; i< input1; i++)

                {

                        if(max < input2[i][0]) 

                                max = input2[i][0];

                        sum += input2[i][1] - max;

                        max = input2[i][1];

                }

                return sum;

        }


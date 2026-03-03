function highAndLow(numbers){
  // ...
  let myArr = numbers.split(" ");
  let high = Math.max(...myArr);
  let low = Math.min(...myArr);
  
  return high + " " + low;
}
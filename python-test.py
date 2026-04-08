// f1: returns elements from array a at even indices up to b
function f1(a, b) {
  let result = [];
  for (let i = 0; i < b; i++) {
    if (i % 2 === 0) {
      result.push(a[i]);
    }
  }
  return result;
}

// f2: returns the sum of elements divisible by 3
function f2(a) {
  return a.filter(i => i % 3 === 0)
          .reduce((sum, val) => sum + val, 0);
}

// f3: returns squares of elements in a whose indices are not in b
function f3(a, b) {
  let c = [];
  for (let i = 0; i < a.length; i++) {
    if (!b.includes(i)) {
      c.push(a[i] ** 2);
    }
  }
  return c;
}

// f4: returns an object with element counts
function f4(a) {
  let result = {};
  [...new Set(a)].forEach(i => {
    result[i] = a.filter(x => x === i).length;
  });
  return result;
}

// f5: multiply elements in a that also exist in b by random integer 1–10
function f5(a, b) {
  return a
    .filter(i => b.includes(i))
    .map(i => i * (Math.floor(Math.random() * 10) + 1));
}

// f6: find pairs whose sum is zero
function f6(a) {
  let result = [];
  for (let i = 0; i < a.length; i++) {
    for (let j = i + 1; j < a.length; j++) {
      if (a[i] + a[j] === 0) {
        result.push([a[i], a[j]]);
      }
    }
  }
  return result;
}

function main() {
  let x = Array.from({ length: 10 }, (_, i) => i);
  let y = Array.from({ length: 5 }, (_, i) => i);

  let res1 = f1(x, 5);
  let res2 = f2(x);
  let res3 = f3(x, y);
  let res4 = f4(x);
  let res5 = f5(x, y);
  let res6 = f6(x);

  console.log(res1);
  console.log(res2);
  console.log(res3);
  console.log(res4);
  console.log(res5);
  console.log(res6);
}

main();
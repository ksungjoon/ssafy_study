// 함수 선언식

function kakao(age) {
    console.log(age);
}
kakao(99)

// 함수 표현식
const naver=function(age) {
    console.log(age);
}
naver(41)



// 차이점
// 함수 선언식은 - 호이스팅이 발생
// 함수 선언식은 출력을 위에서 할수 있음
kakao(99)
function kakao(age) {
    console.log(age);
}
// 그 이유로 함수 선언식보다 함수 표현식을 권장

// arrow function

const naver1=age => console.log(age)
naver1(41);

// 함수 표현식을 에로우펑션으로 작성한것

// 매개변수가 한개면 가로 생략 가능 한개가 아니면 가로생략 불가능

const naver2=(age) => console.log(age)
naver2(41);

// 안에 있는 식이 한개면 {} 생략가능 그렇지 않으면 불가능

// const google = (age) => console.log(age+10)
// google(40)

const google =age => age+10
console.log(google(40));

// 1.function 대신 화살표 => 씀
// 2. 매개변수가 1개면 () 생략 가능 에어비엔비 스타일에서는 넣음
// 3. 매개변수가 필요 없다면 그냥 () 또는 _ 로 표시
// 4. 만약에 한수 안에 식이 1개라면 {} 그리고 return 도 생략 가능


//------------------------------------------------------------

// default argument
const google2 =(age,age2=40) => age+10
// 함수 - 매개변수가 불일치해도 상관없음 - 버그 안띄움
const daum=(age,age2) => {console.log(age,age2)}

daum(12,64,13,6)

// 함수 - 매개변수 spread 연산자도 사용가능
const yahoo = (age, ...rest)=> {console.log(age)}

yahoo(12,64,13,6,56);

// --------------------------------------------------------------

// 즉시실행함수(일회용함수)
// 한번만 실행하고 없어지는 함수
// (function(매개변수){
//     console.log('A')
// })(인자값);

(function(num){console.log(num**3)})(2);

// 즉시 실행함수는 한번의 실행만 필요로 하는 초기화 코드부분에 많이 사용된다.
// 그 이유는 변수를 전역으로 너무 많이 선언하는 것을 피하기 위해서이다.
// 전역에 변수를 추가하지 않아도 되기 때문에 코드 충돌없이 구현할 수있다.
// 즉시 실행함수를 할때는 위에 전문장에서 ; 로 안끝나면버그남


// 배열

const a = [1,2,3,4,5]
a.reverse();
a.push(6,7,[1,2,3]); // 맨뒤 추가
console.log(a);
a.pop() // 맨뒤제거
console.log(a);
a.unshift(9); // 맨 앞에 추가
console.log(a);
a.shift(); // 맨 앞 제거
console.log(a);

const result =a.indexOf(3);  // 해당 값의 인덱스 반환
console.log(result);  

const result2 = a.includes(23); // 값의 존재 여부 확인 true or false
console.log(result2);

const ret = a.join('/'); 
console.log(ret);

// 헬퍼 메소드 // 고차 함수
// 콜백함수가 뭐?? 함수 매개변수의 인자값으로 들어가는 함수를 콜백함수라 한다.

// forEach
// map
// filter
// reduce
// find
// some
// every

// forEach (for문 돌리는것과 유사함 그러나 break continue 안됨)

// const num=[8,5,2,1]
// num.forEach(ele=>console.log(ele)); // 함수 arrow function 으로 표현

// num.forEach(function test(ele){console.log(ele)}); // 함수 선언식으로 표현

// 아래와 같은 거임

// for(let x=0;x<num.length;x++){
//     console.log(num[x])
// }

const num = [8,5,2,1]
let num2 =[]

for (let x=0; x<num.length; x++){
    num2.push(num[x]*2)
}
console.log(num2)

// map 사용해서 2 곱한 값을 num2에 담기
const t = num.map(ele=>ele*2)
console.log(t)

// 짝수만 리스트에 담아보자
num2 = []
for (let x=0;x<num.length;x++){
    if (num[x]%2===0){
        num2.push(num[x])
    }
}
console.log(num2)

// filter 를 사용해서 간단하게 해결해 보자 // true 값만 반환!!
const f = num.filter(ele=>ele%2==0)
console.log(f)

// [연습문제] type이 'fruit'인 것들의 name을 모두 출력해보자

const products = [
    {name:'cucumber', type:'vegetable'},
    {name:'banana', type:'fruit'},
    {name:'carrot', type:'vegetable'},
    {name:'apple', type:'fruit'},
]
const answer = products.filter(ele=>ele.type=='fruit');
console.log(answer)

const ans = answer.map(ele=>ele.name)
console.log(ans)

// find 메소드 사용
const num3=[8,9,5,11,12,9];

const j = 9;
const findj = num3.find(ele=>ele===j);
console.log(findj)
// 찾는 값이 없으면 undefined 값 출력
// 찾는 값 찾으면 바로 그 값 출력

// const num3=[8,9,5,1,2,9] 안에 값이 모두 3보다 큰지 확인
// 모두 3보다 크면 true 그게 아니면 false 반환
const e= num3.every(ele=>ele>3)
console.log(e)

// const num=[8,9,5,1,2,9] 안에 값이 하나라도 3보다 큰지 확인
const s = num3.some(ele=>ele>223)
console.log(s)


// reduce - 누적값을 사용할때 사용
const num4 =[8,9,5,11,12,9]
let sum = 0;
for (let x=0;x<num4.length;x++){
    sum+=num4[x]
}
console.log(sum)

const getsum = num4.reduce((acc,cur)=>acc+=cur,0)
console.log(getsum)

// acc = 누적값을 의미
// cur = 순회되는 값을 의미
// ,0 = acc에 들어갈 초기값 셋팅 (0일경우 생략 가능)

// 문자열
let str ="aasdf"
const x = str.includes('s');  // 문자 존재여부 확인
console.log(x);

const x1=str.split('');
console.log(x1);

const x2=str.replace('s','Z');
console.log(x2)

const x3=str.replaceAll('a','yy');
console.log(x3)

let str2="   d   asdf   d    "
console.log(str2)
let b=str2.trim(' ') // 앞뒤 공백 없에기
console.log(b)
let c=str2.replaceAll(' ','')// 모든 공백 없애기
console.log(c)
let d=str2.trimStart(' ') // trimStart는 앞에 공백만 제거 trimEnd는 뒷공백 제거
console.log(d)


// 객체 object
fastfood ={
    a:1,
    "bbq":"gold_olive",
    "ham burger":{
        b:1,
        c:2
    },
    // abc:function(){
    //     console.log('hi')
    // },                             // 메서드 선언시 function 생략 가능함 !!
    abc(){
        console.log('hi')
    }
}
console.log(fastfood.a)

console.log(fastfood["ham burger"].c)
// 띄어쓰기는 . 으로 표현 불가능

console.log(fastfood.bbq)
fastfood.abc();


// 객체 object2

const friends = ['keivin', 'jorny', 'kate']
const age = [27,29,25]

// 객체 key값을 동적으로 활요이 가능하다.


let index=1;
const school = {
    // friends:friends,
    // age:age,
    // 만약에 key값과 할당하는 변수의 이름이 같다면
    // 축약이 가능하다. <속성명 축약>
    friends,
    age,
    [friends[index]]:age[index]
}

console.log(school)

// 객체문법1 : 메서드명 축약(functio 안써도 됨)
// 객체문법2 : key값을 동적으로 가능
// 객체문법3 : 속성명 축약( key 값과 할당받는변수이름이 같을 경우)
// 객체문법4 : destrcturing 

// 객체문법4 : destrcturing
// 변수 또는 객체를 분해해서
// 변수를 하나 만emsrhtdp 할당 하는것

const user={
    name1:'minho',
    name2:'bbq',
    gender:'male',
}

console.log(user.name1,user.gender)

// 변수 선언 후에 객체value를 담아서 출력해보자
// 만약에 변수명과 객체의 key값이 같다면.. 아래와 같이 표현가능
const{name1}=user; // const name1=user.name1
const{gender}=user; // const gender=user.gender

// const{name1,gender}=user;
console.log(name1,gender);


// 객체문법5 : spread

const user1 =['kevin','jorny','kate']
console.log(...user1)

const ban={
    name3:'kfc',
    name4:'MC',
}

const user2 ={
    name1:'minho',
    name2:'bbq',
    ...ban
}
console.log(user2)

// json을 자바스크립트 객체로 
// 자바스크립트 객체를 json 형태로 바꾸기..

const kk = {
    name1:'minho',
    name2:'bbq',
    gender:'male',
    test:[1,2,3,4],
}

console.log(kk)
// json 형식에는 자바스크립트와 다르게 key에는 반드시 쌍따옴표가 들어감!!
// 그래서 자바스크립트 객체를 json 형태로 반환할때
// key 값에 쌍따옴표를 넣어줘야 한다
// 이때 json.stringify를 사용해서 객체를 string 화 시킨후 json형태로 변환이된다

const OBJ_to_Json = JSON.stringify(kk)
console.log(OBJ_to_Json);
console.log(typeof OBJ_to_Json)


const json_to_OBJ= JSON.parse(OBJ_to_Json)
console.log(json_to_OBJ)
console.log(typeof json_to_OBJ)

// 객체에서 this
// this -> 자기참조 변수....

// 결론부터 말하자면 this는 어떤 방식으로 호출 되었는가에 따라서 의미하는것 이 달라진다.

//1. 일반함수에서 호출되었을때  : 전역객체인 window를 의미함
//2. 매서드로 호출 되었을때   : 매서드 호출한 "그" 객체를 의미
//3. 생성자함수에서 호출이 되었을때  : "미래에 생성될 인스턴스"를 의미한다.

//1. 일반함수에서 호출되었을때  : 전역객체인 window를 의미함

const fc=()=>{console.log(this)}  // 일반함수에서 사용한 this
console.log(this) // 전역에서 this 출력했을때

// window 브라우저에서의 최상위 객체를 의미함..


//2. 매서드로 호출 되었을때   : 매서드 호출한(품고있는) "그" 객체를 의미

const obj ={
    a:1,
    b(){
        console.log(this)
    },
}

obj.b();

//3. 생성자함수에서 호출이 되었을때  : this가 의미하는 것은 "미래에 생성될 인스턴스"를 의미한다.

//key가 name이고 value가 choi 인 객체를 3개만든다면...

const a1={
    name1: "choi",
}
const b1={
    name1: "choi",
}
const c1={
    name1: "choi",
}

// 조금더 효율적으로 객체를 찍어내보자
// 이때 생성자 함수 사용..

function Test(name){
    this.name=name
}

const d1 = new Test('choi')
const e1 = new Test('choi')
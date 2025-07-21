import express from 'express'

const app = express()
const port = 3000

const myLogger = function (req, res, next) {
  console.log('LOGGED');
  next();
};

app.use(myLogger);
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/about',(req,res)=>
{
  res.json({message : "success", test : "lol"})
})

app.get('/plain',(req,res) =>
{
  res.set('Content-Type','plain/text')
  res.send("Plain text sended!");
})


app.post('/data', (req,res) =>
{
  console.log("received data:", req.body)
  res.status(201);
  res.json({
    message: "dati ricevuti",
    data: req.body
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
  console.log(`
  Route available:
  '/'       return a string,
  '/about'  return a JSON object
  '/plain'  return a string with Content-type set to plain/text
  '/data'   send JSON data
  `)
})

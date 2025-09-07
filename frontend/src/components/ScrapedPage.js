import { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import { Interceptor } from '../interceptor/axiosInterceptor';

import { Alert, Card, Col, Container, Row, Button, Form} from 'react-bootstrap';

const isDev = process.env.REACT_APP_IS_DEV === 'true';
const URL = isDev ? 'http://localhost:3020/api/scraped_products' :  '/api/scraped_products';
const URL_SCRAPED = 'http://localhost:3060/orchestrate/'

//invocazione dell interceptor che aggiunge il token bearer ad ogni richiesta
Interceptor();

const ScrapedPage = () => {
    
    
    const [products, setScrapedProducts] = useState([]); // List of all products
    const [message, setMessage] = useState(''); // Success/Error messages
    
    const [searchQuery, setSearchQuery] = useState(''); // Stato per il nome prodotto
    const [selectedCategory, setSelectedCategory] = useState('');

    const [isLoading, setLoading] = useState(false); // Simulazione Caricamento bottone
    
    const fetchScrapedProducts = async () => {
        try {
            const response = await axios.get(`${URL}`);
            setScrapedProducts(Array.isArray(response.data) ? response.data : []);
        } catch (error) {
            setMessage('Failed to fetch scraped products');
        }
    };

    // Funzione per gestire il submit del form
    const handleScrapedSubmit = async (e) => {
        e.preventDefault();
        console.log('Categoria: ', selectedCategory);
        console.log('Nome prodotto: ', searchQuery);
        setLoading(true);
        try {
            const response = await axios.get(`${URL_SCRAPED}${selectedCategory}`,{
                params : {
                    'q': searchQuery
                }
            } 
            );
            console.log("url: ", response.config.url)
            setScrapedProducts(Array.isArray(response.data) ? response.data : []);
            fetchScrapedProducts()
            setMessage('')
            console.log(response.data)
        } catch (error) {
            setMessage('Failed to fetch scraped products');
        } finally {
        setLoading(false);
    }
    };

    return (

        <Container>
            <div className="text-center mt-3 mb-4">
                <h2 className="fw-bold">Scraping prodotti da Subito.it</h2>
                <p className="text-muted">
                    Inserisci il nome del prodotto e seleziona una categoria per cercare gli annunci più recenti su Subito.it.
                </p>
            </div>
            <Form onSubmit={handleScrapedSubmit} className="mb-4 p-3 bg-light rounded shadow-sm">
                <Form.Select 
                    aria-label="select_value"
                    value={selectedCategory}
                    onChange={e => setSelectedCategory(e.target.value)}    
                >
                    <option value="usato">Seleziona una categoria</option>
                    <option value="elettronica">Elettronica</option>
                    <option value="informatica">Informatica</option>
                    <option value="telefonia">Telefonia</option>
                    <option value="videogiochi">Console e videogiochi</option>
                    <option value="casa-e-persona">casa e persona</option>
                    <option value="sport-hobby">Sport e Hobby</option>
                    <option value="annunci-vari">Altri</option>

                </Form.Select>
                
                {/* Campo input per il nome prodotto */}
                <Form.Control
                    type="text"
                    placeholder="Nome prodotto"
                    value={searchQuery}
                    onChange={e => setSearchQuery(e.target.value)}
                    disabled={isLoading}
                    className="my-3"
                />
                <Button variant="primary" type='submit'> {isLoading ? 'Loading…' : 'Scrape'}</Button>
            </Form>

            <hr className="mb-4" />

            {/* <h1>Product Management</h1> */}
            {message && <Alert variant="info">{message}</Alert>}
            
            <Row>
            {products.length > 0 ? (
                products.map((product) => (
                <Col key={product._id} sm={12} md={6} lg={4} className="mb-4">
                    <Card style={{ width: '18rem' }}>
                        <Card.Body>
                            <Card.Title>{product.title}</Card.Title>
                            <Card.Subtitle className="mb-2 text-muted">
                                {product.price_not_specified ? "Price not specified" : `$${product.price}`}
                            </Card.Subtitle>
                            <Card.Text>
                                <strong>Location:</strong> {product.city}({product.province})
                            </Card.Text>
                            <Card.Text>
                                <strong>Date Scraped:</strong> {new Date(product.date_scraped).toLocaleDateString()}
                            </Card.Text>
                            <Card.Text>
                                <strong>Shipping:</strong> {product.shipping_available ? "Available" : "Not available"}
                            </Card.Text>
                            <Card.Text>
                                <a href={product.url} target="_blank" rel="noopener noreferrer">View Original</a>
                            </Card.Text>
                            <small className="text-muted">ID: {product._id}</small>
                        </Card.Body>
                    </Card>
                </Col>
                ))
            ) : (
                <div className="text-center">
                    <p>No products available</p>
                </div>
            )}
            </Row>
        </Container>
    )
};

export default ScrapedPage;



// db_products=# SELECT * FROM scraped_products;
//  _id | title | city | date_scraped  | price | province | url | shipping_available | price_not_specified

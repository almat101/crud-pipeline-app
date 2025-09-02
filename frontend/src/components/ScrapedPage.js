import { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import { Interceptor } from '../interceptor/axiosInterceptor';

import { Alert, Card, Col, Container, Row} from 'react-bootstrap';

const isDev = process.env.REACT_APP_IS_DEV === 'true';
const URL = isDev ? 'http://localhost:3020/api/scraped_products' :  '/api/scraped_products';


//invocazione dell interceptor che aggiunge il token bearer ad ogni richiesta
Interceptor();

const ScrapedPage = () => {
          
    const [products, setProducts] = useState([]); // List of all products
    const [message, setMessage] = useState(''); // Success/Error messages

    
    const fetchScrapedProducts = useCallback(async () => {
        try {
            const response = await axios.get(`${URL}`);
            setProducts(Array.isArray(response.data) ? response.data : []);
        } catch (error) {
            setMessage('Failed to fetch products');
        }
    },[]);
    

    useEffect(() => {
            fetchScrapedProducts();
    }, [fetchScrapedProducts ]);

    return (

        <Container>
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
                                <strong>Location:</strong> {product.city}, {product.province}
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

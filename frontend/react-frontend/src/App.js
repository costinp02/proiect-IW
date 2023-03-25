import React, { useEffect, useState } from 'react';
import './App.css';
import Products from './components/Products';
import PostLoadingComponent from './components/PostLoading';

function App() {
	const PostLoading = PostLoadingComponent(Products);
	const [appState, setAppState] = useState({
		loading: false,
		products: null,
	});
  useEffect(() => {
		setAppState({ loading: true });
		const apiUrl = `http://localhost:8000/api/products/`;
		fetch(apiUrl)
			.then((data) => data.json())
			.then((products) => {
				setAppState({ loading: false, products: products });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Our Products</h1>
			<PostLoading isLoading={appState.loading} posts={appState.products} />
		</div>
	);

}

export default App;
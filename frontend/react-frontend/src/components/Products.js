import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	productTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	productText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Products = (props) => {
	const { products: products } = props;
	const classes = useStyles();
	if (!products || products.length === 0) return <p>Can not find any posts, sorry</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Paper className={classes.root}>
					<TableContainer className={classes.container}>
						<Table stickyHeader aria-label="sticky table">
							<TableHead>
								<TableRow>
									<TableCell>Id</TableCell>
									<TableCell align="left">Type</TableCell>
									<TableCell align="left">Name</TableCell>
									<TableCell align="left">Desription</TableCell>
                                    <TableCell align="left">Expiry Date</TableCell>
                                    <TableCell align="left">Price</TableCell>
								</TableRow>
							</TableHead>
							<TableBody>
								{products['results'].map((product) => {
									return (
										<TableRow>
											<TableCell component="th" scope="row">{product.id} </TableCell>
											<TableCell align="left">{getProductType(product.type)}</TableCell>
											<TableCell align="left">{product.name} </TableCell>
                                            <TableCell component="th" scope="row">{product.description} </TableCell>
                                            <TableCell align="left">{product.expiry_date} </TableCell>
                                            <TableCell align="left">{product.price} </TableCell>                
										</TableRow>
									);
								})}
								
							</TableBody>
						</Table>
					</TableContainer>
				</Paper>
			</Container>
		</React.Fragment>
	);
};

function getProductType(productType){
    switch(productType){
        case "CA":
            return "Capsules";
            break;
        case "DR":
            return "Drops";
            break;
        case "PO":
            return "Powder";
            break;
        case "LI":
            return "Liquid";
            break;
        case "TA":
            return "Tablets";
            break;
        case "OT":
            return "Other";
            break;

    }

}
export default Products;
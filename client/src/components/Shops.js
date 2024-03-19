import React from "react";
import AddShopForm from "./AddShopForm"

function Shops({ shopsList, clickHandler, isLoaded, refresh }) {

  if (!isLoaded) return <h3>Loading...</h3>

	return (
		<div className="shops">
			<h1>Shop Page</h1>

			<h3>Shop List</h3>
			<ul>
				{shopsList.map(shop => {
					const {id, name} = shop
					return (
						<li key={id}>
							{name}
							&nbsp;&nbsp;&nbsp;
							<button onClick={() => {
								clickHandler(id);
							}}>x</button>
						</li>
					)
				})}
			</ul>

			<AddShopForm refresh={refresh} />

		</div>
	)
}

export default Shops
import model, repository

def test_repository_can_save_a_batch(session):
    batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)
     
    repo = repository.SqlAlchemyRepository(session)
    repo.add(batch)
    session.commit()

    rows = list(
        session.execute(
            "SELECT reference, sku, _purchased_quantity, eta FROM 'batches'"
        )
    )
    assert rows == [("batch1", "RUSTY-SOAPDISH", 100, None)]

def insert_order_line(session):
    session.execute(
        "INSERT INTO order_lines (orderid, sku, qty)"
        " VALUES ('order1', 'GENERIC-SOFA', 12)"
    )
    [[orderline_id]] = session.execute(
        "SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku",
        dict(orderid="order1", sku="GENERIC-SOFA")
    )
    return orderline_id

def insert_batch(session, batch_id): ...

def test_repository_can_retrieve_a_batch_with_allocations(session):
    orderline_id = insert_order_line(session)
    batch1_id = insert_batch(session, "batch1")
    insert_batch(session, "batch2")
    insert_allocation(session, orderline_id, batch1_id)
    
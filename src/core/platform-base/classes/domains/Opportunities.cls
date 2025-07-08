public inherited sharing abstract class Opportunities {
	protected List<Opportunity> opportunities;

	public List<Opportunity> getRecords() {
		return this.opportunities;
	}

	public Map<Id, Account> parentAccountsByIds {
		get{
			if (parentAccountsByIds==null) {
				parentAccountsByIds=getParentAccountByIds();
			}
			return parentAccountsByIds;
		}
		set;
	}

	public Map<Id, User> opportunityOwnersByIds {
		get{
			if (opportunityOwnersByIds==null) {
				opportunityOwnersByIds = getOpportunityOwnersByIds();
			}
			return opportunityOwnersByIds;
		}
		private set;
	}

	public Boolean isEmpty(){
		return this.opportunities.isEmpty();
	}

	public Integer size(){
		return this.opportunities.size();
	}

	public Map<Id, Account> getParentAccountByIds(){
		Set<Id> accountIds = new Set<Id>();
		for (Opportunity opportunity:this.opportunities){
			accountIds.add(opportunity.AccountId);
		}
		return new Map<Id, Account>([SELECT Industry, NumberOfEmployees FROM Account WHERE Id IN: accountIds]);
	}

	public Map<Id, User> getOpportunityOwnersByIds(){
		Set<Id> ownerIds = new Set<Id>();
		for (Opportunity opportunity:this.opportunities){
			ownerIds.add(opportunity.OwnerId);
		}
		return new Map<Id, User>([SELECT Country FROM User WHERE Id IN:ownerIds]);
	}
}